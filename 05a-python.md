# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar as they are both sequences of values of any type. The difference is that tuples are immutable meaning you can't modify the elements of the tuple only replace one tuple with another. On the other hand lists are mutable and the values can be changed.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> List and sets both contain values as opposed to dictionaties which have keys with values associated with them. Lists are ordered sets are not. Sets require a hash value which is a value associated to the objects that remains for its lifetime. You cannot have duplicates in sets so you are required to use lists in that case or remove the duplicates. Sets are much faster in finding an element than a list because a list must be gone through from start to finish so depending on the length of the list it can take a very long time.

List: [1,2,3,4,5]
Set: (['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is an anonymous python function that takes any number of arguments (including optional arguments) and returns the value of a single expression. It removes the need to have a function--it's basically a function without a name so it cant be called later but can do the job in a single line.

def p(x):
  return x**2
p(2)
4

y = lambda x: x**2
y(2)
4

key=lambda variable: variable[0]
sorts by the first variable
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





