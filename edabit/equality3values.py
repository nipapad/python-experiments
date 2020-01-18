"""a function that takes three integer arguments (a, b, c) and
returns the number of equal values. must return 0, 2 or 3."""
def equal(a,b,c):
    numbers = [a,b,c]
    if numbers.count(a)==3: return 3
    if numbers.count(b)==2: return 2
    return 0
    
