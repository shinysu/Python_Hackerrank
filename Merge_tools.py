'''https://www.hackerrank.com/challenges/merge-the-tools/problem'''


def merge_the_tools(string, k):
    t = []
    unique_word = []

    for i in range(0, len(string), k):
        t.append(string[i:i + k])
    for word in t:
        newword=[]
        for i in range(k):
            if word[i] not in newword:
                newword.append(word[i])
        unique_word.append(''.join(newword))
    print("\n".join(unique_word))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)