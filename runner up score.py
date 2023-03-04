if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=list(arr)
    m=max(arr1)
    print(m)
    ind=arr1.index(m)
    arr1.pop(ind)
    print(arr1)
    for i in arr1:
        if i==m:
            indx=arr1.index(i)
            arr1.pop(indx)

print(max(arr1))
