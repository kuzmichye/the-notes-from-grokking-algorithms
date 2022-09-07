def binary_search(array,item):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        guess = array[mid]
        if guess== item:
            return True
        if guess>item:
            right = mid - 1
        else:
           left = mid+1
    return None
