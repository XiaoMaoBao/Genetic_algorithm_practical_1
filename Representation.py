import string
import random

class String:
    def __init__(self, binary_str) -> None:
        self.binary_str = binary_str
        self.fitness_score = 0

    def count(self, s):
        return self.binary_str.count(s)

    def slice(self, lb, ub):
        return self.binary_str[lb: ub]

    def __repr__(self) -> str:
        return self.binary_str



def count_ones(binary_str: String):
    return binary_str.count('1')

#counting ones eval
#



#deceptive trap function *1
#

def DeceptiveTight(binary_str: string):
    sumScore = 0
    mapping = [x*4 for x in range(1,11)]
    #print("The string: ", binary_str)

    for index in mapping:
        substring = binary_str.slice((index-4), (index))
        number_ones = substring.count('1')
        #print("lb", index-4)
        #print("ub", index)

        tp_score = DeceptiveTP(number_ones)

        sumScore += tp_score
        #print("Substring: ", substring)
        #print("Number ones: ", number_ones)
        #print("NonDeceptive TP score:", tp_score)
    #print("Sum score: ",sumScore)

    return sumScore
        

def NonDeceptiveTight(binary_str: string):
    sumScore = 0
    mapping = [x*4 for x in range(1,11)]
    #print("The string: ", binary_str)

    for index in mapping:
        substring = binary_str.slice((index-4), (index))
        number_ones = substring.count('1')
        #print("lb", index-4)
        #print("ub", index)

        tp_score = NonDeceptiveTP(number_ones)

        sumScore += tp_score
        #print("Substring: ", substring)
        #print("Number ones: ", number_ones)
        #print("NonDeceptive TP score:", tp_score)
    #print("Sum score: ",sumScore)

    return sumScore
        

def DeceptiveLoose(binary_str: string):
    sumScore = 0
    for index  in range(1,11):
        subString = ''

        for mult in [0,10,20,30]:
            i = (index+mult)
            subChar = binary_str.slice((i-1),i)
            subString = subString + subChar
    
        tp_score = DeceptiveTP(subString.count('1'))

        sumScore += tp_score
    return sumScore


def NonDeceptiveLoose(binary_str: string):
    sumScore = 0
    for index  in range(1,11):
        subString = ''

        for mult in [0,10,20,30]:
            i = (index+mult)
            subChar = binary_str.slice((i-1),i)
            subString = subString + subChar
    
        tp_score = NonDeceptiveTP(subString.count('1'))

        sumScore += tp_score
    return sumScore



def DeceptiveTP(argument):
    switcher = {
        0: 3,
        1: 2,
        2: 1,
        3: 0,
        4: 4,
    }
    return switcher.get(argument, 0)


def NonDeceptiveTP(argument):
    switcher = {
        0: 1.5,
        1: 1.0,
        2: 0.5,
        3: 0,
        4: 4,
    }
    return switcher.get(argument, 0)