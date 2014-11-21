def sum_tree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sum_tree(x)
    return tot
    

#print(sum_tree([1, [2, [3, 4], 5], 6, [7, 8]]))
#print(sum_tree([1, [2, [3, [4, [5]]]]]))
#print(sum_tree([[[[[1], 2], 3], 4], 5]))

#the same as breadth-first search, use queue instead of recursion
def queue_sum_tree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)      
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot
    
#print(queue_sum_tree([[[[[1], 2], 3], 4], 5]))

#the same as depth-first search, use stack instead of recursion
def stack_sum_tree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)      
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot
    
#print(stack_sum_tree([[[[[1], 2], 3], 4], 5]))