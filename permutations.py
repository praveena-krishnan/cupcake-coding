from itertools import permutations
if __name__ == '__main__':
    string, k = input().split()
    l1=sorted(list(itertools.permutations(string,int(k))))
    for i in l1:
        print("".join(i))
