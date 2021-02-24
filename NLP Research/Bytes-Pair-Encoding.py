# Byte Pair Encoding
import collections
import re

def get_corpus(PATH_FILE):
    """Lấy ra các word và format theo BPE

    Mọi word sẽ được format về dạng word('char char char </w>')
    
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
    """Encode word theo vocabulary

    word: string chưa được token
    sorted_tokens: tập vocabulary các token được sorted DESC
    unk_token: unknown token

    return word đã được token theo BPE
    """
    if word == '':
        return []
    if sorted_tokens == []:
        return [unk_token]

    word_tokened = []
    for i in range(len(sorted_tokens)):
        token = sorted_tokens[i]
        token_reg = re.escape(token)
        matched_positions = [(m.start(), m.end()) for m in re.finditer(token_reg, word)]
        if len(matched_positions) == 0:
            continue
        subword_end_positions = [pos[0] for pos in matched_positions]
        subword_start_position = 0
        for subword_end_position in subword_end_positions:
            subword_prev = word[subword_start_position:subword_end_position]
            word_tokened += encode_word(subword_prev, sorted_tokens[i+1:])
            word_tokened += [token]
            subword_start_position = subword_end_position + len(token)
        subword_remain = word[subword_start_position:]
        word_tokened += encode_word(subword_remain, sorted_tokens[i+1:])
        break
    return word_tokened

if __name__ == '__main__':
    # đọc file -> lấy corpus
    corpus = get_corpus('path_file')
    num_merge = 1000

    # xây dựng tập vocab gồm các token
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

    # sort các token theo cả len token và frequency
    sorted_tokens_tuple = sorted(vocab.items(), 
                                key=lambda item: (get_len_token(item[0]), item[1]),
                                reverse=True)
    li_tokens_sorted = [token for (token, freq) in sorted_tokens_tuple]

    # demo tokenize word theo BPE
    demo_word = 'Ilikeeatingapples!</w>'
    if demo_word in known_word_tokenized:
        print(f'word tokenized = {demo_word}')
    else:
        word_encoded = encode_word(demo_word, li_tokens_sorted)
        print(f'word tokenized = {word_encoded}')

