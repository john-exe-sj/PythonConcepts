"""
Operators allow us to form conditional expressions that resolve to True or False AKA Boolean Values.

Operators: 
    < Less Than
    > Greater Than
    >= Greater than or equal to
    <= Less than or equal
    != Not equal to
    == equal to
    and (Requires both conditional expressions to be true)
    or (Allows for one conditional expression to be true)
    not (Creates 'the opposite' of the conditional expression)
"""

johnIsHungry = True
cond_1 = 1 == 1 # True
cond_2 = 3.5 < 4 # True
cond_3 = "bay" == "Bay" # False
cond_4 = johnIsHungry == False # False
cond_5 = 100 >= 101 # False
cond_6 = "John" != "JOHN" # True
cond_7 = "John" == "John" # True
cond_8 = "John has a dog" != "John has a dsog" # False

if johnIsHungry:  
    print("John is indeed hungry")

if cond_1: 
    print("1 == 1", cond_1)

johnIsHungry = False
if not johnIsHungry: 
    print("John is no longer hungry.")

a = cond_1 or cond_2
b = cond_5 and cond_6
print("a's result", a)
print("b's result", b)

if a: 
    print("a's result is True")

# First exposure to an if-else, if the above condition expression, the else's code will execute instead.  
if b: 
    print("b's result is True")
else: 
    print("reminder, b's result was:", b)


