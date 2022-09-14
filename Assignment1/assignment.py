"""Replace the word 'pass' with your solution!"""

from array import array
from itertools import count
import math
from statistics import mean, median
STUDENT_NAME = "Kristian Myzeqari"
STUDENT_ID = "261037094"


def q1(x, y):
    """Write a function that returns the sum of x and y"""

    return x+y


def q2(x, y):
    """Write a function that returns the product of x and y"""
    return x*y


def q3(x, y):
    """Write a function that returns the value of x to the y power"""
    return x**y


def q4(x):
    """Write a function that returns the 3 computed values 
    in a tuple or list form:

    x times 2, x minus 3, and x divided by 10 (integer-division, not floating point)
    """
    i = x*2
    j = x-3
    k = x//10
    array1 = (i, j, k)
    return array1


def q5(x, y):
    """Write a function to represent the summation from the assignment doc"""
    result = 0
    for x in range(y+1):
        result = result + x
    return result


def q6(x):
    """Write a function to represent the following summation, while being given x as input:

    Hint: You do not need to use the answer in q5 for this question.
    """
    result = 0
    i = 0
    j = 0
    for i in range(x+1):
        for j in range(6):
            result = result + (2*i + j)
    return result


def q7(x):
    """Create and return a list of integers (length x) where:

    * The absolute value of each element is three times the index. 
    For example, the absolute value of the element at index 5 should be 15.

    * Values at even indices must be positive, and values at odd indices must be negative.

    The output should resemble this format: 

    If x=5, then output = [0, -3, 6, -9, 12] 

    Hint: Nothing should be printed in this question, as we ask you to return the list of values. 

    """
    result = []

    for i in range(x):

        result.append(((-1)**i)*i*3)
    return result


def q8(lst):
    """Create a function to find the index of every number 10 
    within the given input list, 'lst'. 

    Return these indices as a new list.

    (hint: use 'enumerate')

    Examples:
    lst: [10, 9, 8, 7, 6, 10, 4, 3, 10, 1]
    answer: [0, 5, 8]

    lst: [10]
    answer: [0]

    lst: [3, 2, 1]
    answer: []

    lst: []
    answer: []
    """
    result = []
    count = 0

    for i in range(len(lst)):
        if lst[i] == 10:
            result.append(i)
    return result


def q9(dct):
    """Determine the GPA of the given student, using the given dict 'dct'.
    The keys of the dict are course names, while the values are the GPA obtained in each course. 

    Return two things as a tuple: a list of the courses taken, and the semester GPA. You can 
    assume that all courses pull the same weight in the GPA calculation, i.e., it is sufficient 
    to compute the average of the GPAs to determine the semester GPA. 

    (hint: 2.6 is very similar to 2.59999996 so either answer should be fine. We use math.isclose)
    (hint 2: use dict.items)

    Examples:
    input: {'Calc 2' : 2.3, 'Physics' : 3.4, 'Algorithms' : 2.1}
    answer: (['Calc 2', 'Physics', 'Algorithms'], 2.6)

    input: {'English' : 1.5, 'History' : 4.0, 'French' : 3.8}
    answer: (['English', 'History', 'French'], 3.1)
    """
    result = []
    gpa = 0
    
    keys = list(dct.keys())
    values = list(dct.values())
    count = 0

    for i in range(len(values)):
        count += values[i]
    return keys, count/len(values)

def q10(x):
    """Create a function that performs the following operations on the given input x:
    if x less than 5 or greater than 255, return 0
    if x is between 5 and 255 (inclusive), return x divided by 1.25 (floating-point division)
    """
    if x<5 or x>=256:
        return 0
    else:
        return x/1.25

def q11(x, y, z):
    """Create a function that performs vector normalization on the 3D vector <x, y, z>

    Return a list or tuple of the 3 normalized x, y, z values.

    The formula for vector normalization is in the assignment doc.

    (hint: use the math python module)

    Examples:
    input: [4, 5, 6]
    answer (not exact): [0.4558423058385518, 0.5698028822981898, 0.6837634587578276]

    input: [3, 4, 0]
    answer: [0.6, 0.8, 0.0]

    input: [0, 100, 0]
    answer: [0, 1, 0]
    """
    vectorLength = math.sqrt((x**2)+(y**2)+(z**2))
    print(vectorLength)
    print(x/vectorLength)

    return x/vectorLength, y/vectorLength, z/vectorLength


def q12(radius, degrees):
    """Write a funciton to convert the given Polar Coordinates into Cartesian Coordinates. 
    These formulas are in the assignment doc.

    (hint 1: The input is in DEGREES but you need RADIANS)

    (hint 2: both math.cos and math.sin USE RADIANS)

    input: [10, 60]
    answer (not exact): (5.000000000000001, 8.660254037844386)

    input: [10, 30]
    answer: (8.660254037844387, 4.999999999999999)

    input: [1, 180]
    answer: (-1.0, 1.2246467991473532e-16)

    input: [13, 22.6]
    answer: (12.001732822468751, 4.9958391945774485)

    """
    angleInRadians = (degrees*2*math.pi)/360
    x = radius*(math.cos(angleInRadians))
    y = radius*(math.sin(angleInRadians))
    return x, y


def q13(data: list[list[int]]):
    """From a list of lists of numbers, give the Minimum, Maximum, Mean, and Median for each list in the given data.

    The format of these lists is as follows:
    [
        [1,2,3,4,5],
        [3,4,5],
        [45,83,65,52,47]
    ]
    The number of give lists is variable, and the length of each list is variable.
    Your code will not be tested for speed performance.

    Output your data as a string. Each list's stats are in one row, which is separated by a newline character.
    Each number is separated by a comma, such as this:
    1,2,3,4
    6,7,8,9
    1,2,3,4
    3,6,8,9

    Do not use print(). Create and build the string in a variable and return the string.
    No extra spaces. You may end each row with a newline.(Your testing program will expect this)
    """

    result = ""
    for i in range (len(data)):
        minimum = str(min(data[i]))
        maximum = str(max(data[i]))
        average = str(mean(data[i]))
        medval = str(median(data[i]))
        result = result + minimum + "," + maximum + "," + average + "," + medval + "\n"
    return result

def q14(text: str):
    """Take the following string input and convert it into a 2-dimensional list. Such as:

    Input:
    1,2,3
    4,5,6,7,8
    9,102,5,25,3

    Output:
    [
        [1,2,3],
        [4,5,6,7,8],
        [9,102,5,25,3]
    ]

    Requirement:
    * The numbers within the 2D list output must be of the int type, not the str type.

    Rules for Input Data:
    * The input string will not have any spaces in it.
    * Each row is separated by a newline character.
    * There is no newline character at the end of the Input String.
    * Each number is separated by a comma.
    * The numbers will all be integers within -2147483648 to 2147483647.
    """
    output = []
    tempList = []
    for i in text:
        if i == '\n': 
            output.append(tempList)
            tempList = []
        else: 
            if i != ',':
                j = int(i)
                tempList.append(j)
    output.append(tempList)
    print(output)
    return output
