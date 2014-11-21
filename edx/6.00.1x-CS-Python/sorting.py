import operator
import string

def mergeSort(t, compare = operator.lt):
    if len(t) == 1:
        return t
    
    mid = len(t) / 2
    left = mergeSort(t[:mid], compare)
    right = mergeSort(t[mid:], compare)
    
    return merge(left, right, compare)
    
def merge(left, right, compare):
    r = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1
        
    while i < len(left):
        r.append(left[i])
        i += 1
        
    while j < len(right):
        r.append(right[j])
        j += 1

    return r

def selectionSort(t, compare = operator.lt):
    for i in range(len(t) - 1):
        minIdx = i
        minVal = t[i]
        j = i + 1
        while j < len(t):
            if compare(t[j], minVal):
                minVal = t[j]
                minIdx = j
            j += 1
        temp = t[i]
        t[i] = t[minIdx]
        t[minIdx] = temp
        
    return t
    
def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26
    
t = [1, 5, 2, 17, 10, 9, 11, 6, 3, -12]
print mergeSort(t, operator.lt)
print selectionSort(t, operator.gt)

print hash('abcdef')
print hash('aabb')