import turtle
import math
import random

tur = turtle.Turtle()
turtle.speed(10)
turtle.tracer(False)
screen = turtle.Screen()
screen.setworldcoordinates(175, -100, screen.window_width() -175, screen.window_height() - 100)
screen.bgcolor("yellow")
tur.color("white")


# Custom dictionary class for adding dictionary key and value
class my_dictionary(dict):
    def __init__(self):
        self = dict()
    
    def add(self,keys,values):
        self[keys] = values

dict_object = my_dictionary()


def collatz(times):
  sequence_key = 0
  while sequence_key != times:
    num = math.floor(random.randint(2,9999)) # collatz conjecture initial number range
    sequence = []
    while num!=1:
        if(num%2==0):
            num = num/2
        else:
            num = (3*num) + 1
        if not num in sequence:
            sequence.append(num)
    else:
        sequence.append(1)
        sequence_key+=1
        dict_object.add(sequence_key,sequence) 
  return dict_object
    

# Graph the collatz conjecture
def graph(times):
    dict = collatz(times)
    dot_size = 5
    margin_size_x = 2.25
    margin_size_y = 50
    amount_nums = 0
    even_nums = 0
    odd_nums = 0
    for key in dict:
        for sequence_index in range(len(dict[key])-1):
            # get x,y point by getting number and multiplying by margin size
            x = (sequence_index*margin_size_x)
            y = math.floor((math.log(dict[key][sequence_index])*margin_size_y))
            tur.penup()
            tur.goto(x,y)

            # Evens and Odd and Colors
            if(dict[key][sequence_index] % 2 ==0):
                tur.dot(dot_size, "blue")
                even_nums+=1
            else:
                tur.dot(dot_size, "red")
                odd_nums+=1
                
            amount_nums+=1
    # Extra information about all the times conjecture ran. Fun Fact: even:odd is 2:1
    print("Amount Nums", amount_nums)
    print("Evens", even_nums)
    print("Odds", odd_nums)

    
graph(100) # how many times do you want the conjecture to run?
turtle.done()
