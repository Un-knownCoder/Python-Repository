## Input and Output

### Input:
Well... In python input is really simple, as you just need to write a single function:

```py
variable = input("Enter a value for this variable... ")
# Now, when the user hits enter, the variable will be filled with the entered value

# <!> Note that in the 'input' function there is a string...
#     ... that string is displayed in a console line once you can input the variable value
```

Since there isn't a real variable typing, the input value will be considered as a string, so,
if you want to operate with user entered **NOT STRING** values you **MUST** cast the input

```py
var1 = input("Enter a string... ")
# user >> "hello world" ::: the variable is now a string with "hello world" inside

var2 = int(input("Enter a number... "))
# user >> 12345 ::: the variable is now an integer with 12345 inside
# if the input can't be parsed as an integer, the program throws an error

var3 = tuple(input("Enter a string"))
# user >> "abcde" ::: the variable is now a tuple with ("a", "b", "c", "d", "e") inside
```
<br />

### Output
As the input, also output is really simple, in fact you just need to write the function `print(...)`

```py
var = input("Write something about you... ")
print("user said: " + var)

# Here's an example of input and output
# In the 'print' function were used a string concatenation
```

> **Watch Out!!!** Since the string concatenation needs to be made of strings only, you need to cast to string every single variable you are using

```py
var = int(input("Write your favourite number..."))
print("user said: " + var) # This will throw an error during the execution

# You must write the function in this way
print("user said: " + str(var))

```
