# 🐍 Chapter 04: Functions


## 📝 Core Concepts

### To function or not to function...
* Organize your code into "paragraphs" - capture a complete thought and "name it".
* Don't repeat yourself - make it work once and then reuse it.
* If something gets too long or complex, break it into logical chunks and put those chunks in functions.
* Make a library of common stuff that you do over and over.



### Function Definition
* In Python a function is some reusable code that takes arguments as input, does some computation, and then returns a result or results.
* We define a function using the def reserved word.
* We call/invoke the function by using the function name, parentheses, and arguments in an expression.

---

### Functions Types  in Python: 
* Built-in functions e.g. print(), input(), type(), float(), int().
* Functions that we define ourselves and then use.

---

### Type Conversions
* When you put an integre and floating point in an expression, the integer is impplicitly converted to a float.
* You can control this with the built-in functions int() and float().

---

### String Conversions
* You can also use int() and float() to convert between strings and integers.
* You will get an error if the string does not contain numeric characters.

---

### Building Own Funtions
* A new function is created by using the def keyword followed by optional parameters in parentheses.
* Indent the body ot the function.
* This defines the function but doesn't execute the body of the function.

---

### Definitions and Uses
* Once we have defined a function, we can call (or invoke) it as many times as we like.
* This is the store and reuse pattern.

---

e.g. **[Print Lyrics](https://github.com/olha-yatskivska/python-lessons/functions/exercises/print-lyrics.py)**  

---

### Arguments 
* An arguments is a value we pass into the function as its input when we call the function.
* We use arguments so we can direct the function to do different kinds of work when we call it at different times.
* We put the arguments in parentheses after the name of the function: big = max('Hello world').

---
### Parameters
* A parameter is a variable which we use in the function definition.
* It's a "handle" that allows the code in the function to access the arguments for a particular function invocation.

---

### Return Values
* Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression.
* The return keyword is used for this.
  >>> def greet(lang):
       if lang = 'es':
          return = 'Hola'
       elif lang = 'fr':
          return = "Bonjour'
       else:
          return 'Hello'
  >>> print(greet('en'), 'Glenn')
  Hello Glenn
  >>> print(greet('es'), 'Sally')
  Hello Sally
  >>> print(greet('fr'), 'Michael')
  Hello Michael

  * A "fruitful" function is one that produces a result (or return value).
  * The return statement ends the function execution and "send back" the result of the function. 

---

### Multiple Parameters / Arguments
* We can define more than one paremrter in the function definition.
* We simply add more arguments when we call the function.
* We match the number and order of arguments and parameters:
  def addtwo(a,b):
       added = a + b
       return added

  x = addtwo(3, 5)
  print(x)

  8
---

### Void (non-fruitful) Functions
* When a function doesn't return a value, we call it a "void" function.
* Fuction that return values are "fruitful" functions
* Void functions are "not fruitful"
  













