
def sumOfTwo(arr, s):
    begin = 0
    end = len(arr)-1
    result = []
    while (begin < end):
        if arr[begin] + arr[end] == s:
            result.append((arr[begin], arr[end]))
            begin += 1
        else:
            if arr[begin] + arr[end] > s:
                end -= 1
            else:
                begin += 1
    return result

if __name__ == '__main__':
    arr = [1, 2, 4, 5, 9, 11, 15]
    s = 13
    l = sumOfTwo(arr, s)
    print (l)
