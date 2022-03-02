import string
import random

class String:
    def __init__(self, binary_str) -> None:
        self.binary_str = binary_str

    def count(self, s):
        return self.binary_str.count(s)

    def slice(self, lb, ub):
        return self.binary_str[lb: ub]

    def __repr__(self) -> str:
        return self.binary_str

def count_ones(binary_str: String):
    return binary_str.count('1')


def DeceptiveTight(binary_str: string):
    sumScore = 0
    mapping = [x*4 for x in range(1,11)]
    print("The string: ", binary_str)

    for index in mapping:
        substring = binary_str.slice((index-4), (index))
        number_ones = substring.count('1')
        print("lb", index-4)
        print("ub", index)

        tp_score = DeceptiveTP(number_ones)

        sumScore += tp_score
        print("Substring: ", substring)
        print("Number ones: ", number_ones)
        print("NonDeceptive TP score:", tp_score)
    print("Sum score: ",sumScore)

    return sumScore
        

def NonDeceptiveTight(binary_str: string):
    sumScore = 0
    mapping = [x*4 for x in range(1,11)]
    print("The string: ", binary_str)

    for index in mapping:
        substring = binary_str.sliceString((index-4), (index))
        number_ones = substring.count('1')
        print("lb", index-4)
        print("ub", index)

        tp_score = NonDeceptiveTP(number_ones)

        sumScore += tp_score
        print("Substring: ", substring)
        print("Number ones: ", number_ones)
        print("NonDeceptive TP score:", tp_score)
    print("Sum score: ",sumScore)

    return sumScore
        

def DeceptiveLoose(binary_str: string):
    pass

def NonDeceptiveLoose(binary_str: string):
    pass

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