
def add_poly(poly1, poly2):
    temp1 = list(poly1)
    temp2 = list(poly2)
    if len(temp1) < len(temp2):
        temp = temp2
        for i in range(len(temp1)):
            temp[i] += temp1[i]
    else:
        temp = temp1
        for i in range(len(temp2)):
            temp[i] += temp2[i]
    return temp

def sub_poly(poly1,poly2):
    temp1 = list(poly1)
    temp2 = list(poly2)
    if len(temp1) < len(temp2):
        temp = temp2
        for i in range(len(temp1)):
            temp[i] -= temp1[i]
    else:
        temp = temp1
        for i in range(len(temp2)):
            temp[i] -= temp2[i]
    return temp

def mul_poly(poly1,poly2):
    temp1 = list(poly1)
    temp2 = list(poly2)
    temp = [0]*(len(temp1)+len(temp2)-1)
    for i in range(len(temp1)):
        for j in range(len(temp2)):
            temp[i+j] += temp1[i]*temp2[j]
    return temp

def is_zero(poly):
    for i in poly:
        if i==0:
            pass
        else:
            return False
    return True

def cmp_poly(poly1,poly2):
    temp1 = list(poly1)
    temp2 = list(poly2)
    if is_zero(temp1) or is_zero(temp2):
        if is_zero(temp1) and is_zero(temp2):
            return True
        return False
    if len(temp1) != len(temp2):
        if len(temp1)>len(temp2):
            for i in range(len(temp2), len(temp1)):
                if temp1[i] != 0:
                    return False
        else:
            for i in range(len(temp1), len(temp2)):
                if temp2[i] != 0:
                    return False
    for i in range(len(temp1)):
       if temp1[i] != temp2[i]:
            return False
    return True

def eval_poly(poly, x0):
    temp = list(poly)
    result = 0
    for coefficient in reversed(temp):
        result = result * x0 + coefficient
    return result

def combine_poly(poly1, poly2):
    temp1 = list(poly1)
    temp2 = list(poly2)
    i = len(temp1) - 1
    temp = [temp1[i]]
    while i > 0:
        i = i - 1
        temp = add_poly(mul_poly(temp, temp2),[temp1[i]])
    return temp

def pow_poly(poly, n):
    temp1 = list(poly)
    temp = [1]
    while n > 0:
        temp = mul_poly(temp, temp1)
        n = n - 1
    return temp

def diff_poly(poly):
    return [poly[i] * i for i in range(1, len(poly))]

cmp_poly([4,8,1],[4,8,1])
