def find_similar_words(n, sentence, word):
    words = sentence.split()
    similar_words = []
    
    for w in words:
        word1 = word
        w1 = w
        if len(w) < len(word):
            w1 += "_" * (len(word) - len(w))
        elif len(w) > len(word):
            word1 += "_" * (len(w) - len(word))
        distance = sum(c1 != c2 for c1, c2 in zip(w1, word1))
        if distance <= n:
            similar_words.append(w)
    return similar_words

n = int(input())
sentence = input()
sentence = sentence.replace('.', '')
sentence = sentence.replace('،', '')
sentence = sentence.replace(':', '')
word = input()

result = find_similar_words(n, sentence, word)

for i in range (len(result)):
    print(result[i])
