'''https://www.hackerrank.com/challenges/merge-the-tools/problem'''
import collections

def merge_the_tools(string, k):
    t = []
    unique_word = []

    for i in range(0, len(string), k):
        t.append(string[i:i + k])
    for word in t:
        word = "".join(collections.OrderedDict.fromkeys(word))
        print(word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
