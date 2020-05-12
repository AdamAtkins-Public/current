import os

def intCoefOfVarience(L):
    mean = sum(L)/len(L)
    var_sum = int(0)
    for i in L:
        var_sum += (i - mean)**2
    standard_deviation = (var_sum/len(L))**0.5
    return standard_deviation/mean

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    
    sum_total = int(0)
    for word in L:
        sum_total += len(word)
    mean = sum_total/len(L)
    var_sum = int(0)
    for word in L:
        var_sum += (len(word)-mean)**2
    varience = var_sum/len(L)
    return varience**0.5

if __name__ == '__main__':
    print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
    print(stdDevOfLengths([]))
    print(intCoefOfVarience([10, 4, 12, 15, 20, 5]))