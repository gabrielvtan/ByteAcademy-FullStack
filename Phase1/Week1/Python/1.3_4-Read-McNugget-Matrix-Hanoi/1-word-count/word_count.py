from operator import itemgetter
from collections import Counter


def word_counts(filename, number):
    counter = Counter()
    with open(filename, 'r') as input_file:
        for line in input_file:
            for word in line.split():
                counter[word] +=1
                word_counts = counter
    for word, count in word_counts.most_common(number):
        print("{}: {}".format(word,count))

if __name__ == "__main__":
    wcounts = word_counts('article.txt', 5)
    # now how do you display your data?
