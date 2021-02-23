# Byte Pair Encoding
import collections
import re

def get_corpus(PATH_FILE):
    """Lấy ra các word và format theo BPE

    Mọi word sẽ được format về dạng string('char char char </w>')
    
    word <- 'char char char </w>'
    num <- số lần xuất hiện của word đó trong toàn corpus 

    return dict([word_1: num, word_2: num,...])
    """
    corpus = collections.defaultdict(int)
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            charaters = line.strip().split()
            for char in charaters:
                corpus[' '.join(char) + '</w>'] += 1
    return corpus

def get_stats(corpus):
    """Thống kê tần suất theo cặp của toàn bộ character trong corpus

        return defaultdict(int,
                           {('char', 'char'): int,
                            ('char', 'char'): int,
                            (...)})
    """
    pairs = collections.defaultdict(int)
    for word, freq in corpus.items():
        char = word.split()
        for i in range(len(char) - 1):
            pairs[char[i], char[i + 1]] += freq
    return pairs

def update_corpus(pair, corpus):
    """Gộp cặp character có tần suất xuất hiện nhiều nhất và update trên toàn corpus

       pair: cặp character có tần suất xuất hiện lớn nhất trong corpus
       corpus: chứa các word và frequency của word đó

       return new_corpus sau khi đã merge cặp character này trên tất cả các word của corpus
    """
    new_corpus = collections.defaultdict(int)
    format_char = re.escape(' '.join(pair)) 
    pattern = re.compile(r"(?<!\S)" + format_char + r"(?!\S)") # 2 kí tự đứng trước và sau format_char phải là khoảng trắng(space) -> _format-char_
    for word in corpus:
        new_word = re.sub(pattern, ''.join(pair), word) # replace merged_pair trên từng sentence
        new_corpus[new_word] = corpus[word]
    return new_corpus

def get_vocab(corpus):
    """Lấy ra danh sách tất cả các token từ corpus và tokenize của một word

    corpus: {word: freq, word: freq, word: freq,...}
    vocab: {token: freq, token: freq, token: freq,...}
    known_word_tokenization: {word: word_tokenized, word: word_tokenized,...}

    return vocab, known_word_tokenization

    """
    vocab = collections.defaultdict(int)
    known_word_tokenization = collections.defaultdict(str)
    for word, freq in corpus.items():
        word_tokens = word.split()
        for token in word_tokens:
            vocab[token] += freq
        known_word_tokenization[word] = word_tokens
    return vocab, known_word_tokenization

def get_len_token(token):
    """Lấy ra độ dài của token
    """
    if token[-4:] == '</w>':
        return len(token[:-4]) + 1
    else:
        return len(token)

def decode_word(word_tokened):
    """Decode word đã được token

       word_tokened: [token, token, token,...]
       return word: string
    """
    word = ''.join(word_tokened)
    word_decoded = word.replace('</w>', ' ')
    return word_decoded

def encode_word(word, sorted_tokens, unk_token='<UNK>'):
    """Encode word
    """
    pass

if __name__ == '__main__':
    corpus = get_corpus('path_file')
    num_merge = 1000
    for i in range(num_merge):
        pairs = get_stats(corpus)
        if not pairs:
            break
        best_pair = max(pairs, key=pairs.get)
        corpus = update_corpus(best_pair, corpus)
        vocab, known_word_tokenized = get_vocab(corpus)
        print(f'iter: {i}')
        print(f'best pair = {best_pair}')
        print(f'number of vocab = {len(vocab)}')
        print(f'list vocabularies = {vocab}')
        print('===================================')

    sorted_tokens_tuple = sorted(vocab.items(), 
                                key=lambda item: (get_len_token(item[0]), item[1]),
                                reverse=True) # sort các token theo cả len token và frequency
    li_tokens_sorted = [token for (token, freq) in sorted_tokens_tuple]

    demo_word = 'Ilikeeatingapples!</w>'
    if demo_word in known_word_tokenized:
        print(f'word tokenized = {demo_word}')
    else:
        encode_word(demo_word, li_tokens_sorted)

