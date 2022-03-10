#kaitlyn bauer

import math
#problem 1
#x= int(input('pick a number: '))
def is_even(x):
    if (x % 2) == 0:
        print('true')
    else:
        print('false')
        
#is_even(x)
#problem 2
#x = float(input('pick a number: '))
def is_int(x):
    if (x % 1) == 0:
        print('true')
        
    else:
        print('false')
#is_int(x)

#problem 3
#x = int(input('what number do you want the sum of: '))     
def digit_sum(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum
#print(digit_sum(x))

#problem 4   
#x = int(input('Chose a number to factorial: '))
#print(int(math.factorial(x)))

#problem 5
#x = int(input('Pick a number: '))
F = "Your number is not prime"
T = "Your number is prime"
def is_prime(x):
    if x <= 1:
        return F
    else:
        for number in range (2, x):
            if x % number == 0:
                return F  
    return T
#print(is_prime(x))

#problem 6
#x = input('Enter a string of text to reverse: ')
#def reverse(x):
    final = ''
    for i in x:
        final = i + final
        return final
#print(reverse(x))


#problem 7
#string = input('choose a word: ')
#def antivowel(string):
    new = string;
    vowels = ['a', 'e' , 'i' , 'o' , 'u']
    text_input = ''
    for x in string:
        if x not in vowels:
            text_input = text_input + x
    return text_input
#print(antivowel(string))

#problem 8
#word = str(input('what word do you want to scrabble score: '))
#score = {'a':1 , 'b':4 , 'c':4 , 'd':2 , 'e':1 , 'f':4 , 'g':3 , 'h':3 , 'i':1 , 'j':10 , 'k':5 , 'l':2 , 'm':4 , 'n':2 , 'o':1 , 'p':4, 'q':10, 'r':1, 's':1, 't':1 , 'u':2 , 'v':5 , 'w':4, 'x':8 , 'y':3, 'z':10}
def scrabble_score(word):
    sum = 0
    for x in word:
        for item in score:
            if x.lower() == item:
                sum += score[item]
                print(str(item) + ':' + (str(score[item])))
    return sum
#print(scrabble_score(word))

#probelem 9
#def censor(text, word):
    text = text.split
    for i in range (0, len(text)):
        #if text(i) = word:
           # text(i) = '*'*len(text(i))
        return ''.join(text)
#print(censor('this'))

#probelem 10
#def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total = total +1
    return total
#print(count((3, 2, 1, 2, 3), 1))
#probelem 11
#def purify(numbers):
    flist = []
    for i in numbers:
        if i % 2 == 0:
            flist.append(i)
    return flist
#print(purify(1,2,3))
#probelem 12
#def product(x):
    total = 1
    for i in x:
        total = total*1
    return total
#print(product[4, 5, 6])

#problem 12
#def remove_duplicates(x):
    alist = []
    for i in x:
        if i not in alist:
            alist.append(i)
    return alist
#print(remove_duplicates(1, 1, 2, 2))
