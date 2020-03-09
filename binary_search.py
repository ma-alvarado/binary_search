#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    left = 0
    right = len(xs)-1
    if xs == []:
        return('None')
    if len(xs) == 1:
        if xs[0] > 0:
            return 0
    if len(xs) == 2:
            if xs[left] > 0:
                return 0
            elif xs[right] > 0:
                return 1
            elif xs[left] <= 0 and xs[right] <= 0:
                return 'None'
    def go(left,right):
        mid = (left+right)//2
        if left == right:
            if xs[right] < 0:
                return 'None'
        if 0 < xs[mid]:
            right = mid - 1
        if 0 > xs[mid]:
            left = mid + 1
        if 0 ==xs[mid]:
            return mid + 1
        if left == right and 0 != xs[mid]:
            if right == 0:
                if xs[right+1] < 0:
                    return 'None'
                else:
                    return mid 
            else:
                if xs[right] < 0:
                    return 'None'
                else:
                    return mid
        return go(left,right)
    return go(left,right)



def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    low = lowest_index(xs,x)
    high = highest_index(xs,x)

    print(low)
    print(high)

    if low == 0 and high == 0 or (low == high and xs[0] != x):
        return 0
    if len(xs) == 1 and xs[0] == x:
        return 1
    else:
        return high - low + 1


    

def highest_index(xs,x):
    left = 0
    right = len(xs) - 1
    if xs == []:
        return 0
    def go(left,right):
        mid = (left+right)//2
        if right - left == 0:
            if xs[right] != x:
                return 0
            if xs[right] == x:
                return 1
        if right - left == 1:
            if xs[right] != x and xs[left] != x:
                return 0
            if(xs[right] != x):
                return left
            else:
                return right
        if left == right:
            if xs[right] < 0:
                return 0
        if x < xs[mid]:
            left = mid
        if x > xs[mid]:
            right = mid
        if x ==xs[mid]:
            left = mid
        return go(left,right)
    return go(left,right)


def lowest_index(xs,x):
    left = 0
    right = len(xs) - 1
    if xs == []:
        return 0
    def go(left,right):
        mid = (left+right)//2
        if right - left == 0:
            if xs[right] != x:
                return 0
            if xs[right] == x:
                return 1
        if right - left == 1:
            if xs[right] != x and xs[left] != x:
                return 0
                
            if(xs[mid] == x):
                return left
            else:
                return right
        if left == right:
            if xs[right] < 0:
                return 0
        if x < xs[mid]:
            left = mid
        if x > xs[mid]:
            right = mid
        if x ==xs[mid]:
            right = mid
        return go(left,right)
    return go(left,right)



def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''


    left = lo
    right = hi
    def stop(left,right):

        m1 = ((right - left) // 3) + left 
        m2 = ((right - left) // 2) + left

        if (right - left) < epsilon:
            return right

        if f(m1) < f(m2):
            stop(left,m2)
      
        if f(m2) < f(m1):
            stop(m1,right)






