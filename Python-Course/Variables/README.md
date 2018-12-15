## Variables

In python there isn't any variable type specification, in fact you just need to write the variable name followed by an equal sign and a value to give it the first assignment:
```py
num = 10               # a numeric variable
string = "Hello World" # a string variable

array = [1, 2, 3]      # an array (list) variable

tuple = (1, 3, 2)      # a tuple variable is similar to a list,
                       # but it hasn't a real structure
```

However this notation also creates some problems ... 
<br /> ... as you can imagine you can overwrite the variables with a different type from the one declared at the first assignment
<br /> So be **really** carefull when you assign values to variables!!!

```py
variable = "hi, i'm a variable!" # First declaration [string]

variable = 10                    # this is NOT an error, and now the variable is an integer
variable = (1, 2)                # ... and now a tuple
```
