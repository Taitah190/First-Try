# Name: Ke Xu
# CptS 111, Spring 2020
# Programming Assignment: 5
# Date: 3/13/2020
# Name of program: gold_ratio
# In this programe, we calculate the standard division of a set of numbers

def get_float():
    n = int(input('enter the number of list elements'))
    e = []
    i = 0
    for double in range(n, 0, -1):
        num = float(input('enter a float number here'))
        e.append(num)
    return e
def summer(e):
    s = 0
    for i in e:
        s = s+i
        l = len(e)
    return s, l
def average(s, l):
    a = s/l
    return a
def std_dev(e, a, l):
    b = 0
    for i in e:
        d = (i - a)**2
        b = b + d
        squared = b/l
        sd = squared**0.5
    return sd
def main():
    e = get_float()
    s, l = summer(e)
    a = average(s, l)
    sd = std_dev(e, a, l)
    print('average =', a)
    print('Standard deviation=', sd)
main()

    
        
