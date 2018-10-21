def bubblesort(a):
    for i in range(len(a)):
        while i > 0:
            if a[i] < a[i - 1]:
                t = a[i]
                a[i] = a[i - 1]
                a[i - 1] = t
            i -= 1
    return a
