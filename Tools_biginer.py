#print("Hello World")

#Triangle
"""print("   /|")
print("  / |")
print(" /  |")
print("/___|") """

#Types of Variable
""" character_name = "John" #String
character_age = "50" #Number_no_need_of_cotation
is_male = True #boolian
print("There once was a man named " + character_name + ",")
print("he was "+character_age+" years old.")
character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being "+character_age+".") """

#Function
"""phrase="Giraffe Academy"
#print(phrase.upper().isupper())
#print(len(phrase))
#print(phrase[3])
#print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))"""

#number
""""#print(3*(4+5))
#print(10%3)
my_num= -5
#print(str(my_num)+" my favorite number") # can't print number and string together
#print(abs(my_num))
#print(pow(4.2438478,6.23433))
#print(max(4.2438478,6.23433))
#print(round(3.2))

from math import*
#print(floor(3.7))
#print(ceil(3.7))
#print(sqrt(36))"""

#Input from user
"""name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are "+age)"""

#Basic Calculator
"""num1 = input("Enter a number: ") #bydefault python takes varilbe as string
num2 = input("Enter a another number: ")
result = float(num1) + float(num2) # int:whole number, float: fraction
print(result)"""

#Mad Libs Game
"""color = input("Enter a color: ")
plural_noun = input("Enter a plural Noun: ")
celebrity = input("Enter a celebrity: ")
print("Rose are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)"""

#List/Array
"""friends = ["kevin", "karen", "jim","Oscar","Toby"]
#print(friends[1])
#print(friends[-1])
#print(friends[1:])
#print(friends[1:3]) #upto 2
friends[1]="Mike"
print(friends[1])"""

#List Function
"""lucky_numbers = [15, 4, 8, 42, 16, 23]
friends = ["Mevin", "Karen", "Jim","Jim","Oscar","Toby"]
#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.insert(1,"Kelly")
#friends.remove("jim")
#friends.clear()
#friends.pop()
#print(friends)
#print(friends.index("Oscar"))
#print(friends.count("Jim"))
#friends.sort(); print(friends)
#lucky_numbers.sort(); print(lucky_numbers)
#lucky_numbers.reverse(); print(lucky_numbers)
#friends2 = friends.copy(); print(friends2)"""

#Tuples
"""coordinates = [(4,5), (6,7), (80,34)]
coordinates[1]= 10  #Immutable: Can't be modified
print(coordinates[0])"""

#Functions
"""def say_hi(name, age):
    print("Hello "+ name +", you are "+ str(age)) #prints only string or number

say_hi("Luban", 25)"""

#Return Statement
"""def cube(num):
    return num*num*num
    print("code") #out of funtion, neglected as after return

#print(cube(4))
result= cube(4); print(result)"""

#If Statements
"""is_male = False
is_tall = True

if is_male or is_tall: # OR statement
    print("You are a male or tall or both")
else:
    print("Yor are neither male nor tall")"""

"""if is_male and is_tall:  # AND statement
    print("You are a tall male")
else:
    print("Yor are either not male or not tall or both")"""

"""if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("Yor are not male and not tall")"""

#If Statements & Comparisons
"""def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3: #Comparision Operator_true or false condition
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30,6,2))"""

#Building a Better Calculator
"""num1 = float(input("Enter first number: "))  #by default python convert data into string
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1 * num2)
elif op =="/":
    print(num1 / num2)
else:
    print("Invalid Operator")"""

#Dictionaries
"""monthConversions = {
    "Jan": "January",  # "Jan"=key word
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#print(monthConversions["Mar"])
print(monthConversions.get("Luv", "Not a valid key"))"""

#From Youtube
"""import turtle as t
import colorsys

t.bgcolor("black")
t.speed("fastest")
t.tracer(100)
t.pencolor("darkviolet")
hue = 0.7
t.hideturtle()


def func():
    global hue
    for i in range(4):
        global hue
        for i in range(4):
            color = colorsys.hsv_to_rgb(hue, 1, 1)
            hue += 0.001
            t.fillcolor(color)
            t.begin_fill()
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(22)
            t.end_fill()


for j in range(400):
    func()
    t.goto(8, 8)
    t.rt(188)

t.exitonclick()"""

#While Loop
"""i = 0
while i <= 10:
    print(i)
    i += 1
print("Done with Loop")"""

#Building a Guessing Game
"""secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess (Animal): ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You are out of guesses, YOU LOSE!")
else:
    print("You win!")"""

#For Loop
"""friends = ["Jim", "Karen", "Kevin"]
for letter in "Giraffe Academy":  #variable = letter
    print(letter)
for name in friends:
    print(name)
for index in range(3, 10):
    print(index)
for index in range(len(friends)):
    print(friends[index])
num= ["First", "Second", "Third", "Fourth", "Fifth"]
for index in range(5):
    print( num[index] + " iteration")"""

#Exponent Function
"""print(2**3) #2^3
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
base_num = int(input("Enter the base number: "))
pow_num = int(input("Enter the power number: "))
print(raise_to_power(base_num, pow_num))"""

#2D Lists & Nested Loops
number_grid = [
    [1,2,3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#print(number_grid[1][2])
'''for row in number_grid:
    #print(row)
    for col in row:
        print(col)'''

#Build a Translator
"""def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":  #converts all uppercase characters to lowercase. If no uppercase characters exist, it returns the original string
            if letter.isupper():  
                translation = translation + "O"  #translates letter into "O"
            else:
                translation = translation + "o"  #translates letter into "o"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))"""

#Try Except
"""try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  #storing the error in "err" variable
    print(err)
except ValueError:
    print("Invalid Input")  #Handling the Error"""

#Reading Files
"""employee_file = open("employee.txt", "r")  #r for read
#open("employee.txt","w")                  #w for write
#open("employee.txt","a")                  #a for append(adding new information)
#open("employee.txt","r+")                 #r for read and write
#print(employee_file.readable())           #readable() giv boolian value, the file is readable or not
#print(employee_file.read())               #Read the lines
#print(employee_file.readline())           #Reading the first line
#print(employee_file.readline())           #Reading the second line
#print(employee_file.readlines())          #Read all the lines and put them into an list
#print(employee_file.readlines()[1])       #Read the 2nd line in the list
for employee in employee_file.readlines(): #For loop
    print(employee)
employee_file.close()"""                      #Close the "employee.txt" file

#Writing to Files
"""employee_file = open("employee.txt", "a")        #a for append(adding new information)
employee_file.write("Toby - Human Resources")       #add new data at the end of the line
employee_file.write("\nToby - Human Resources")"""  #add new data at new line

"""employee_file = open("employee.txt", "w")        #overrighting on existing file(employee.txt)
employee_file.write("Toby - Human Resources")"""

"""employee_file = open("employee1.txt", "w")       #create and write on new file
employee_file.write("Toby - Human Resources")"""

"""employee_file = open("index.html", "w")           #Create a HTML file
employee_file.write("<p> This is HTML</p>")"""       #Writing on the file

"""employee_file.close()"""

#Modules and Pip
"""import useful_tools                     #import the "useful_tools" file

print(useful_tools.roll_dise(10))"""       #using a function from "useful_tools" file

#Classes & Objects
"""from Student import Student         #First "Student" = file, 2nd "Student" = Class

student1 = Student("jim", "Business", 3.1, False)
student2 = Student("pam", "Art", 2.5, True)
#print(student1.name)
print(student2.gpa)"""

#Building a Multiple Choise Quiz  ###########
"""from Question import Question
question_promts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promts[0],"a"),
    Question(question_promts[1],"c"),
    Question(question_promts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:              ###
        answer = input(question.prompt)     ###
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)"""

#Object Function
"""from Student1 import Student1

student1 = Student1("Oscar", "Accounting", 3.1)
student2 = Student1("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())"""          #using a function defined in class "Student1"

#Inheritance
"""from ChineseChef import ChineseChef      #importing 'ChineseChef' file with inherited 'Chef' file

ChineseChef().make_salad()"""

#Python Interpreter
"""comand prompt"""