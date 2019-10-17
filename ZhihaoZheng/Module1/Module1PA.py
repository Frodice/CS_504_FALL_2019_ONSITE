def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break

def bubble_sort2(alist):
    a = len(alist)
    for j in range(a - 1):
        count = 0
        for i in range(0, a - 1 - j):
            if alist[i] < alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break
        

if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    bubble_sort(alist)
    print("bubble is :%s" % alist)
    bubble_sort2(alist)
    print("bubble2 is :%s" % alist)