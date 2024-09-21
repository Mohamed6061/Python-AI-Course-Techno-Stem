# <!-- Data type -->
# int
# str 
# float
# bool
# dict
# set
# tuple
# list

# string data type
str_var = "This is text"

print(type(str_var))
print(str_var)

# string data type
str_var = "This is text"

print(type(str_var))
print(str_var)

# list data type
list_var = [12 , "text" , True , [ 12,2 ,3] , 12.4]

print(type(list_var))
print(list_var)

# dict data type

dict_var = {
    "one" : 1,
    "two " : 2,
    "skills" : ["python", "html"]
}

print(type(dict_var))
print(dict_var)

# bool data type
bool_var = 50 > 60
print(type(bool_var))
print(bool_var)

# tuple data type 
tuple_var = (12,24,5)
print(type(tuple_var))
print(tuple_var)

# set data type
set_var = { "apple" , "banana" ,12}
print(type(set_var))
print(set_var)

# float data type
float_Var = 12.5
print(type(float_Var))
print(float_Var)

# convert string to  int
x  = "223"
y = int(x)
print(type(y))
print(y)

# convert list to dict
x = [["one", 1] , ["two" , 2] , ["three" , 3 ] ]

y = dict(x)
print(type(y))
print(y)

# int to str

x =12 
y = str(x)
print(type(y))
print(y)

# bool >> int
x = False
y = int(x)

print(y)
print(type(y))

# int ==> bool
x = -123
y = bool(x)
print(y)
print(type(y))

# string methods

txt = "this is text text text "
print(txt[8 : ])
print(txt.upper())
print(txt.lower())

print(txt.split())
print(txt.replace("is" ,"are"))

print(txt.count("x"))
print(txt.capitalize())

# list  ==> str
l = ["this" , "is" , "text"]

print("-".join(l))
txt = "      this is text       "

print(txt.strip())


# methods return ture false- isdigit -islower - isupper
x = "This is text"

print(x.islower())

#  three double quotes
x = """"this line one
this line two
this line three  """

y = "this is \n  \"ahmed\" "

print(y)


# String Format
x =  "Ahmed"
y = 21

print(f"name {x}, age {y}")

# list methods
list_var  = "programming in python is fun"


for element in list_var :
    print(f'this element {element}')

# print(num_list)
# element=  "1"

# Task
text = "programming in python is fun"

c = {"p" : 2 , "r": 2 , }