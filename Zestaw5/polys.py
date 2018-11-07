
def add_poly(poly1, poly2):  
    if len(poly1) < len(poly2):
        temp = poly2
        for i in range(len(poly1)):
            temp[i] += poly1[i]
    else:
        temp = poly1
        for i in range(len(poly2)):
            temp[i] += poly2[i]
    return temp

def sub_poly(poly1,poly2):
    if len(poly1) < len(poly2):
        temp = poly2
        for i in range(len(poly1)):
            temp[i] -= poly1[i]
    else:
        temp = poly1
        for i in range(len(poly2)):
            temp[i] -= poly2[i]
    return temp

def mul_poly(poly1,poly2):
    temp = [0]*(len(poly1)+len(poly2)-1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            temp[i+j] += poly1[i]*poly2[j]
    return temp

def is_zero(poly):
    for i in poly:
        if i==0:
            temp = True
        else:
            temp = False
    return temp

def cmp_poly(poly1,poly2):
    if len(poly1)!=len(poly2) and (not is_zero(poly1) and not is_zero(poly2)):
        return False
    for i in range(len(poly1)-1):
        if poly1[i] == poly2[i]:
            temp = True
        else:
            temp = False
    return temp

def eval_poly(poly, x0):
    result = 0
    for coefficient in reversed(poly):
        result = result * x0 + coefficient
    return result

def combine_poly(poly1, poly2):
    i = len(poly1) - 1
    temp = [poly1[i]]
    while i > 0:
        i = i - 1
        temp = add_poly(mul_poly(temp, poly2),[poly1[i]])
    return temp

def pow_poly(poly, n):
    temp = [1]
    while n > 0:
        temp = mul_poly(temp, poly)
        n = n - 1
    return temp

def diff_poly(poly):
    return [poly[i] * i for i in range(1, len(poly))]
    if len(poly) == 1:
        return [0]
    temp = [poly[i] * i for i in range(1, len(poly))]
    while (len(temp) - 1) > 0 and temp[len(temp) - 1] == 0:
        del temp[len(temp) - 1]
    return temp

