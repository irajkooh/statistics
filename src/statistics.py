import numpy as np
x = np.random.uniform(-10, 10, 100)
x = np.random.normal(-10, 10, 100)
x = [1.2, 2.2, 2.5, 1.0, 15.2, 2.5, 2.2, 2.3, 3.1, 1.4, 2.5, 3.7]
#################################################
def len(x):
    len = 0
    for i in x:
        len = len + 1
    return len
#################################################
def sum(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum
#################################################
def mean(x):
    mean = sum(x) / len(x)
    return mean
#################################################
def std(x):
    import numpy as np
    var = sum([(i-mean(x))**2 for i in x]) /(len(x)-1)
    std = np.sqrt(var)
    return std
#################################################
def mode(x):
    counts = []
    for i in range(len(x)):
        count = 0
        for j in range(len(x)):
            if x[i] == x[j]:
                count = count + 1
        counts.append(count)
        
    for i in range(len(counts)):
        if counts[i] == max(counts):
            mode = x[i]
    return mode
#################################################
def sort(x):
    sorted = x.copy()
    for i in range(len(sorted)):
        for j in range(i+1):
            if sorted[i] < sorted[j]:
                temp = sorted[i]
                sorted[i] = sorted[j]
                sorted[j] = temp
    return sorted
#################################################
def median(x):
    sorted = sort(x)
    for i in sorted:
        if len(sorted) % 2 == 0:
            median = ( sorted[int(len(sorted)/2)-1] + sorted[int(len(sorted)/2)] ) / 2
        else:
            median = sorted[int(len(sorted)/2)]     
    return median
#################################################
def outliers(x): # x should have a normal distribution
    outliers = []
    for i in x:
        z = (i-mean(x)) /std(x) # z is the std of a single data point
        if z > 3:
            outliers.append(i)
    return outliers
#################################################
sorted = sort(x)
percentile = 50 # what is the order of specified percentile ?
order = (percentile/100)*len(sorted)
#################################################
sorted = sort(x)
orderr = 8 # what is percentile of number in specified order ?
m = len(sorted)-orderr
percentilee = ((m+ 0.5)/len(sorted))*100 
#################################################
def power(x, n):
    power = 1
    if n > 0:
        for i in range(n):
            power = power * x
    elif n < 0:
        for i in range(-n):
            power = power * x
        power = 1 / power
    return power
#################################################
def recursive_power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return recursive_power(x, n-1) * x
    elif n < 0:
        n = -n
        return 1 / (recursive_power(x, n-1) * x)
#################################################
def fact(n):
    fact = 1
    if n > 0:
        for i in range(1, n+1):
            fact = fact * i
    elif n < 0:
        fact = 'Negative numbers have no factorial ...'
    return fact
#################################################
def recursive_fact(n):
    if n == 0:
        return 1
    elif n > 0:
        return recursive_fact(n-1) * n
    elif n < 0:
        return 'Negative numbers have no factorial ...'
#################################################
import pandas as pd
x_df = pd.DataFrame(x)
#################################################
print('x      : {}'.format(x))
print('len(x) : {}'.format(len(x)))
print('sum(x) : {:.2f}'.format(sum(x)))
print('mean(x): {:.2f}'.format(mean(x)))
print('std(x) : {:.2f}'.format(std(x)))
print('mode(x): {}'.format(mode(x)))
print('\nsort(x)  : {}'.format(sort(x)))
print('median(x): {}'.format(median(x)))

print('\noutliers(x): {}'.format(outliers(x)))

print('\norder(50)    : {:.0f}'.format(order))
print('percentile(8): {:.0f}'.format(percentilee))

print('\npower(10,  0): {:.2f}'.format(power(10, 0)))
print('power(10,  2): {:.2f}'.format(power(10, 2)))
print('power(10, -2): {:.2f}'.format(power(10, -2)))


print('\nfact(0) : {:.2f}'.format(fact(0)))
print('fact(4) : {:.2f}'.format(fact(4)))
print('fact(-4): {}'.format(fact(-4)))

print(x_df.describe())

# x      : [1.2, 2.2, 2.5, 1.0, 15.2, 2.5, 2.2, 2.3, 3.1, 1.4, 2.5, 3.7]
# len(x) : 12
# sum(x) : 39.80
# mean(x): 3.32
# std(x) : 3.82
# mode(x): 2.5

# sort(x)  : [15.2, 3.7, 3.1, 2.5, 2.5, 2.5, 2.3, 2.2, 2.2, 1.4, 1.2, 1.0]
# median(x): 2.4

# outliers(x): [15.2]

# order(50)    : 6
# percentile(8): 38

# power(10,  0): 1.00
# power(10,  2): 100.00
# power(10, -2): 0.01

# fact(0) : 1.00
# fact(4) : 24.00
# fact(-4): Negative numbers have no factorial ...
#                0
# count  12.000000
# mean    3.316667
# std     3.819289
# min     1.000000
# 25%     2.000000
# 50%     2.400000
# 75%     2.650000
# max    15.200000
