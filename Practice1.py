# [] - used to make a list
# {} - used to make a dictionary
# () - used to ke a tuple.


shopping_list = ["Apples", "Banana", "Grapes", "Oranges"]
print(shopping_list)

shopping_list.append("strawberry") #append function se list k andar kuch bi add kar skte h. because lists are Mutable.
print(shopping_list)

shopping_list[0] = "cherries" #ab isse huMne apples ki jagah cherries kar diya. iska Mtlb jo bi tha index 0 p in the shopping_list wo cheeries M change hojaega.
print(shopping_list)

del shopping_list[2]
print(shopping_list)

print(len(shopping_list))

print(shopping_list[0]) # index always zero se start hota hai naki 1 se 
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[0:4]) #slicing k waqt last index count nhi karte. exclude hojata h

shopping_list2 = ["Bread", "Mayo", "Butter"]

print(shopping_list + shopping_list2)
print(shopping_list * 2)

list_nuM = [1, 2, 3, 4]
print(max(list_nuM))  #predicts the max value from the list
print(min(list_nuM))  #predicts the min value from the list

age = 20, 21, 22
string = "My house is in agra."
print(age[0])
print(string[0:20])
print(string[0:])




# Dictionaries
students = {"Bob": 12, "Rachel": 13, "Emily": 14}
print(students)
print(students["Rachel"])
print(students["Bob"])

students["Rachel"] = 14
print(students)

del students["Rachel"]
print(students)



#Tuples. they are immutable that means they can not be modified once created.
# all the things are pretty similar to that of lists

#1
names = ["Mayank", "Khushboo", "Rupanshi"]
print(names[1])

#2
sports = ["Hockey", "Cricket", "Basketball"]
sports[1] = "Badminton"
print(sports)

#3
nums = [1, 2, 3, 4, 5, 6, 7]
del nums[4]
print(nums)

#4
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]
print(nums1 + nums2)

#5
nums3 = [1, 2, 3, 4, 5, 6, 7]
print(max(nums3))
print(len(nums3))
print(min(nums3))

#6 
students1 = {"Bob":10, "Rachel":9, "Emily":9}
print(students1["Bob"])

#7
students2 = {"Bob":10, "Rachel":9, "Emily":9}
del students2["Rachel"]
print(students2)

#8
students3 = {"Bob":10, "Rachel":9, "Emily":9}
print(students3.keys)
print(students3.values)

#9
movies = ("YJHD", "ZNMD", "DDLJ", "KKHH", "KKKG")
print(movies)

#10
print(movies[0:3])


#Conditional Statents
if 5 > 3:
    print("Hello.")
else:
    print("Conditions was not true.")

#relation operators - > < >= <= == !=
# 5 = 3 mtlb hum 5 ko 3 value assign kar rhe h but ye galat h 5 == 3 karna padega humein

age = 16
if age <= 15:
    print("You are younger than 16")
elif age == 16:
    print("You are 16.")
elif age == 17:
    print("You are 17.")
else:
    print("You are older than 16.")

# Hum multiple if statement laga sakte h elif ko use karke. 

age1 = 2
if age1 < 13:
    print("You are a child.")
elif age1 >= 13 and age1 <= 18:  # and operator m dono conditions true honi chahiye or m bus ek condition dono m se true honi chahiye.
    print("You are a teenager.")
#elif age1 == 2 or age1 == 4:
#    print("You are Baby.")
else:
    print("You are an adult.")


# For loops:

list1 = ['Apples', 'Grapes', 'Bananas']
tup1 = (1, 2, 3)

for item in list1:
    print(item)

for item in tup1:
    print(item)


for i in range(0, 5): #range function se 5 ni print hoga sirf 0,1,2,3,4 because n value jo di h unke alawa karta h just like slicing.
    print(i)

for i in range(0, 5, 2): #range function se huvalues skip bi kar skte hai like 2 mtlb even numbers sirf print honge mtlb jo current number h for ex 0 to next num is 2 like 0 + 2 then 2 + 2 = 4 and so on.
    print(i)

for x in range(0, 26, 5):
    print(x)


#nested for loops;

for q in range (0, 5): # humne ab forloop k andar for loop bana diya h.. iterate karega ab q ki ek value w ki sari value se ltiply then q ki seconf value w ki sari value se ltiply and so on.
    for w in range (5, 10):
        print(q * w)



# While Loops:

c = 0
while c < 5:
    c = c + 1
    if c==3:
        break #comes in handy jub hum apne desired result p poch gye hai and bus wohe tak jana h. Is case m sirf 1 and 2 print hoga and after 2 it terminates
    print(c)


c1 = 0
while c1 < 5:
    c1 = c1 + 1
    if c1 ==3:
        continue #comes in handy jub hum loop continue karna h start se. Ye jaise hi c1 = 3 hoga tub loop aage ki steps ni follow karega that is print but sidha upar chala jaega and start karega shuru se. tow sirf 1,2,4,5 print hoga
    print(c1)


c2 = 0
while c2 < 5:
    c2 = c2 + 1
    if c2 == 3:
        pass #placeholder h bus kuch karta ni hai. baad yaaad aae tow iske jagah kuch aur code chala do ya change kardo.
    print(c2)



#try and except statement
#kafi similar h if and else statements k. agar if hogya thik warna else execute karo. tow same try if wali chiz pehle ni hui to except p jao.

try:
    if name > 3:
        print("Hello.")
except:
    print("Error. Check your code.")



#functions:
#start function with def and then followed by a name. After that ety bracket which indicates that our function doesn't need any input paraters inside the function.

def hello_world():
    print("Hello world!")
# functions needs to be explicitly called to execute its code otherwise we wont get any output so we need to call the function like below.
hello_world()


def greeting(name):
    print("Hi "+ name +"!")

greeting("Mayank")



def function_num(f,g):
    print(f + g)

function_num(2,3)

#return statement
def function_num1(h,i):
    return h + i  #return function_num1 m value store kardega ki h and i ka addition hoga basically and fir wo value hum kahi aur store kar skte haip[]

num1_sum = function_num1(4,5)
print(num1_sum)

def mul(j, k):
    return j * k

print(mul(function_num1(2,3),function_num1(4,5)))





#Python built-in functions

print(abs(-23)) #abs is for absolute value. koi bi negative value ko +ve karne k kaam aata h.
print(bool(0)) #functions as the truth checker. It takes any value and if thta value is 0 or none it gives false otherwise true.
print(bool(None)) #none symbolizes absence of values.
print(bool(100))
print(dir("Hello!")) #tells all the methods one can use with a particular object. shows all the possible methods for string if we put string
print(help('hello'.upper)) #serves as a detailed fescriptionof the requested method.

sent = "print('hi')"
eval(sent) #The eval function is python's way of runningpython code that's disguised as a string
exec(sent) # the EXEC function does sothing very similar to EVAL, but it's designed to execute strings of code spanning multiple lines.

print("Hello " + str(100)) #converts int to string
print(int("112")) #converts string to int
print(float("123.456")) #converts string to float 




# OOP - Classes and Objects

# Class: Dog (defines what a dog is)
# Property: name, breed, age, behaviors
# Methods: bark, eat, sleep

# Objects fido and buddy are two dogs. They might be similar in class and methods but distinct properties. 

class Person:
    def __init__(self, name, age):  #initialize method. The self keyword is a reference to the current instances of this class, and is used to access its attributes.
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

p = Person("Bob", 22)
print(p.getName(), p.getAge())



# OOP - Class Inheritance 

class Car:
    def __init__(self):
        self.wheel = 4
        self.seats = 5

    def drive(self):
        print("Driving a car.")

class SportyCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = "400 HP"
        self.seats = 2

    def drive(self):
        print("Driving a sports car.")


# SportyCar ne kuch chize inherit ki Car class se and then update kara humne kuch kuch like seats and print function.

mySportyCar = SportyCar()
mySportyCar.drive()

