# Byte Pair Encoding
import collections
import re

def get_corpus(PATH_FILE):
    """Lấy ra các sentence và format

    Mọi sentence sẽ được format về dạng string('word word word </w>'), chuẩn bị
    cho BPE
    
    sent <- 'word word word </w>'
    num <- số lần xuất hiện của sentence đó trong toàn corpus 

    return dict([sent_1: num, sent_2: num,...])
    """
    corpus = collections.defaultdict(int)
    with open(PATH_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                corpus[' '.join(word) + '</w>'] += 1
    return corpus

def get_stats(corpus):
    """Thống kê tần suất theo cặp của toàn bộ token trong corpus

        return defaultdict(int,
                           {('d', 'e'): 3,
                            ('g', 'h'): 2,
                            (...)})
    """
    pairs = collections.defaultdict(int)
    for sent, freq in corpus.items():
        word = sent.split()
        for i in range(len(word) - 1):
            pairs[word[i], word[i + 1]] += freq
    return pairs

def merge_vocab(pair, corpus):
    """Gộp các cặp từ có tần suất xuất hiện lớn nhất

       pair: cặp từ có tần suất xuất hiện lớn nhất trong corpus
       corpus: chứa các sentence và frequency của sent đó

       return new_corpus sau khi đã merge cặp từ này trên tất cả các sentence của corpus
    """
    new_corpus = collections.defaultdict(int)
    format_char = re.escape(''.join(pair)) 
    pattern = re.compile(r"(?<\S)" + format_char + r"(?!\S)") # 2 kí tự đứng trước và sau format_char phải là khoảng trắng(space) -> _format-char_
    for sent in corpus:
        new_sent = re.sub(pattern, ''.join(pair), sent)
        new_corpus[new_sent] = corpus[sent]
    return new_corpus

def get_vocab(corpus):
    """Build vocab gồm các token và token frequency từ corpus

       return defaultdict(1,
                          {'token': freq},
                          {'token': freq},
                          {'token': freq},
                          ....)
    """
    tokens = collections.defaultdict(int)
    for word, freq in corpus.items():
        word_tokens = word.split()
        for token in word_tokens:
            tokens[token] += freq
    return tokens

if __name__ == '__main__':
    corpus = get_corpus('path_file')
    num_merge = 1000
    for i in range(num_merge):
        pairs = get_stats(corpus)
        if not pairs:
            break
        best_pair_freq = max(pairs, key=pairs.get)
        corpus = merge_vocab(best_pair_freq, corpus)
        vocab = get_vocab(corpus)
        print(f'vocabulary: {vocab}')

