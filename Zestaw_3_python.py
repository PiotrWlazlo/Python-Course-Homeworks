#Zestaw zadań nr.3

#zad 3.1
# poprawny
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

#bledne zagniezdzenie petli
for i in "qwerty":
    if ord(i) < 100:
        print i


for i in "axby": print ord(i) if ord(i) < 100 else i    #poprawny
#zad 3.2
L = [3, 5, 4] ; L = L.sort() #Nie można jednocześnie przetwarzać  
x, y = 1, 2, 3  #przypisanie trzech wartosci dla dwoch zmiennych
X = 1, 2, 3 ; X[1] = 4  #nie mozna modyfikowac z 'miejsca' krotki (tuple)
X = [1, 2, 3] ; X[3] = 4 #wyjscie poza zakres listy
X = "abc" ; X.append("d") #String nie ma metody append
map(pow, range(8))  #funkcja pow() wymaga dwóch argumentów

#zad 3.3
for i in range(30):
    if not i%3 == 0 or i==0:
        print(i)

#zad 3.4
while True:
    try:
        line = input("Podaj liczbe: ")
        #n = float(line)
        print(n+ ' i ' + pow(float(n), 3))

    except ValueError:
        if line == 'stop':
            break
        print('Nie podales liczby rzeczywistej! Sprobuj jeszcze raz')

#zad 3.5
try:
    length = int(input("Podaj dlugosc miarki: "))
    pattern = "....|"
    linear = ['|', '0']

    linear[0] += (pattern * length)
    for i in range(length):
        linear[1] += "%5s" % (i + 1)

    output = linear[0] + '\n' + linear[1]
    print(output)

except ValueError:
    print("Nie poprawana wartosc")

#zad3.6
x = int(input("Podaj wartosc x: "))
y = int(input("Podaj wartosc y: "))

def generate_line(length, pattern, last_char):
    line = ''
    line += pattern * length
    line += last_char + '\n'
    return line


output = ''
for i in range(y):
    output += generate_line(x, '+---', '+')
    output += generate_line(x, '|   ', '|')

output += generate_line(x, '+---', '+')
print(output)

#3.8
a = [5, 1, 1, 2, 5, 4, 8, 9, 1, 11, 6, 46, 4]
b = [12, 1, 3, 55, 9999, 11]
set_a = set(a)
set_b = set(b)

print(set_a)
print(set_b)

print("Iloczyn zbiorów: ", list(set_a.intersection(set_b)))
print("Suma zbiorów", list(set_a.union(set_b)))
#3.9
sek = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(sek)
print([sum(x) for x in sek])
#3.10
dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(roman):
    arabic_number = 0
    prev = ''
    for i in range(len(roman) - 1, -1, -1):
        if dictionary[roman[i]] < arabic_number and not roman[i] == prev:
            arabic_number -= dictionary[roman[i]]
            prev = roman[i]
        else:
            arabic_number += dictionary[roman[i]]
            prev = roman[i]

    return arabic_number


print(roman2int("XL"))
print(roman2int("IIL"))
print(roman2int("MCCCXXI"))
print(roman2int("MCCC"))

