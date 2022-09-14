def quick_sort(s):
    if len(s)<=1:
        return s
    elem = s[0]
    left = list(filter(lambda x:x<elem,s))
    print(left)
    center = [i for i in s if i==elem]
    print(center)
    right = list(filter(lambda x:x>elem,s))
    print(right)
    return quick_sort(left)+center+quick_sort(right)
print(quick_sort([7,6,10,5,9,8,3,4]))