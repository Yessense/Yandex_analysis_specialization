import re
from collections import Counter
import pandas as pd
from scipy import spatial

import numpy as np
from pandas import DataFrame

sentences = list(map(str.lower, open('sentences.txt', 'r')))
print(sentences)

sentences_s = []
words = set()

for i, sentence in enumerate(sentences):
    c = Counter(re.split('[^a-z]', sentence))
    del (c[''])
    sentences_s.append(dict(c))
    for word in sentences_s[i]:
        words.add(word)

# np.zeros()
print(sentences_s)
print(len(words))
print(len(sentences_s))

frame: DataFrame = pd.DataFrame(np.zeros((len(sentences_s), len(words))), columns=words)
for i, sentence in enumerate(sentences_s):
    for word in sentence:
        frame.loc[i, word] = sentence[word]

print(frame)
distance = []
for i in range(len(sentences_s)):
    distance.append(spatial.distance.cosine(frame.iloc[0], frame.iloc[i]))

frame['Distance'] = distance
print(frame.sort_values(by='Distance'))
result = open('result1.txt', 'w')
result.write('')

