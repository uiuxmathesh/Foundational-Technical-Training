# Day-9 🚀

# Python Day-2 📆

# Agenda

- Expressions vs Statements
- Strings continuation
- Datastructures in Python
    - String
    - List
    - Tuples
    - Dictionaries
    - Set
- Looping statements
    - While-loop
    - For-in loop

### Expressions vs Statements

- Expressions are the line of code which returns a value  or something that we can use for  further computations
    
    Example:
    
    ```sql
    (5+9)/2 - 10 //It returns -3
    ```
    
- Statements are the  ones which does somethinf but does not return anything.
    
    Example
    
    ```sql
    if(5>9): // This will evaluating the condition but never returns anything
    ```
    
    `NOTE` The ternary operator even though it looks llike statement but it is an expression because each ternary operator returns something
    

## Strings (contd…)

### Immutability of  Strings

In general strings are immutable in most programming languages including python. i.e., The values of strings cannot be altered or modified once after  assigning. If we really want to change the value, then we need to reassign the updated string in variable

### Indexing in Python

Like veryother programming  language python indexing of iterables start  with 0. The index of 0 indicates the first element of the array.

Python also supports negative indexing. i.e., you can also access  the elements of the iterables with negative index. negative index starts with -1 and ends at -n where n is  the length of the iterable. The index of -1 denotes the last element, whereas the -n denotes the first element

### String slicing

In python the substring of a string can be easily made without  any methods. This process is called string slicing.

For slicing a string we need to specify from which index of the  existing string do we  want a substring to begin and also specify the ending index which is the ending of the substring

```python
str[startIndex: endIndex: stepValue]
```

Remember, startIndex  is inclusive  and the endIndex is exclusive

The stepValue specifies the gap between each indexes. By default it is set to 1.

```python
string = 'TonyStark'
#usual slicing
string2 = string[2:6] #startIndex = 2 endIndex = 6 #stepValue = default(1) -> "nySt"

#slicing without  startIndex
string3 = string[:4] #startIndex = default(0) endIndex = 4 stepValue = default(0) -> "Tony"

#slicing without endIndex
string4 = string[4:] #startIndex = 4 endIndex = default(n) stepValue = default(1) -> "Stark"

#slicing without bothIndex
string5 = string[:] #startIndex = default(0) endIndex  = default(n) stepValue = default(1) -> "Tony Stark"

#slicing with different stepValue
string6 = string[0:6:2] #startIndex = 0 endIndex = 6 stepValue  = 2 -> "TnS"

#slicing with only  stepValue
string7 = string[::2] # -> "TnSak"
```

## Lists in Python

A list is **a data structure in Python that is a mutable, or changeable, ordered sequence of elements**. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]

Syntax for creating lists

```python
listname = [listitem1, listitem2, listitem3.......]
```

- A list item can be of any type like integer, float, string and even another list.
- The list that contains other lists as list elements are called nested lists

### Methods in Lists

## `List.insert()`

The `insert()` method inserts the specified value at the specified position.

```python
list.insert(pos, elmnt)
```

| Parameter | Description |
| --- | --- |
| pos | Required. A number specifying in which position to insert the value |
| elmnt | Required. An element of any type (string, number, object etc.) |

## `List.append()`

The `append()` method appends an element to the end of the list.

```python
*list*.append(*elmnt*)
```

| Parameter | Description |
| --- | --- |
| elmnt | Required. An element of any type (string, number, object etc.) |

## Combining two lists in python

Two lists can be combined into a single list using `+`  operator in python

```python
list1 = [1,2,3,4]
list2 = [5,6,7,8]

list3 = list1 + list2 #list3 = [1,2,3,4,5,6,7,8]
```

## List Copying

The values of a  list can be copid into another list by multiple ways in python

- Copy-by-reference
- Copy-by-value
- Comprehension

### 1. Copy-by-reference

```python
list1 = [1,2,3,4]
list2 = list1
```

In  the above code we’re creating list2 and copying the values of list1 into list2. This is the simplest form of List copying

But this type of list copying has  some limitation.

```python
list1 = [1,2,3,4,5]
list2 = list1

print(list1) #[1,2,3,4,5]
print(list2) #[1,2,3,4,5]

# Let's change the second element of list2 from 2 to 8
list2 = [1,8,3,4,5]
print(list2) #[1,8,3,4,5]

# Let's also print the list1
print(list1) #[1,8,3,4,5]
```

In the above example  we can see that, even though we updated  the content of `list2` it also changes the value of `list2` . This is because in aliasing both the lists are pointing to the same address. if we try to change a list’s element, then it’ll be reflected in the other lists that are pointing to the same address. This mode of copying is called **Shallow Copy**

### 2. Copy-by-Value

In copy by  value, we use `list.copy()` method to copy a list into another list.

for example,

```python
list1 = [1,2,3,4,5]
list2 = list1.copy()

print(list1)
print(list2)
```

This copies the list items of list1 into list2. Unlike *Copy-by-reference,* this method ensures changing list element from one list does not affect the other. This is because each list is created in separate memory space..

### 3. Comprehension

List Comprehension is the process of copying all the list elements into another list. It’s used to create a python list based on a existing list

```python
list1  =  [1,2,3,4,5,6,7,8,9]
list2  =  [item for item in list1]
```

Let’s see some list methods below.

Consider, `fruits= ['orange','apple','banana']` is the sample  list

| List Methods | Description | Example | Output |
| --- | --- | --- | --- |
| list.append( value) | appends ‘value’ at the end of the list | fruits.append( ‘mango’ ) | ['orange', 'apple', 'banana','mango'] |
| list.insert(value, index) | inserts ’value’ at the ‘index’ | fruits.insert(1, ‘pomegranate’ ) | ['orange', 'pomegranate', 'apple', 'banana'] |
| list.remove( value ) | removes ’value’ from the list.  | fruits.remove( ’apple’ ) | ['orange', 'banana'] |
| list.pop( index ) | removes the value from ‘index’ | fruits.pop( ‘2’ ) | ['orange', 'apple'] |
| list.find( elemet ) | returns the index of the element if it is found inside the list. Otherwise returns -1 | fruits.find( ‘orange’ ) | 0 |

# Conversion of Lists and Strings

## 1. String → List Conversion

- Each string can be converted into list by `split()` method.
- The `split()` method breaks the string based on the given separator.
- You can specify the separator, default separator is any whitespace.
    
    ```python
    String1 = "What a time to be alive!"
    String_list = String1.split()
    print(String_list) #['What','a','time','to','be','alive!']
    
    String_of_colors = "red,blue,green"
    color_list = String_of_colors.split(',') #Specifying a separator
    print(color_list) #['red','green','blue']
    ```
    

## 2. List → String Conversion

- Likewise, each List can be converted into String by `join()` method.
- **Python join()** is an inbuilt string function in Python used to join elements of the sequence separated by a string separator. This function joins elements of a sequence and makes it a string.
    
    ```python
    list1 = ['What','a','time','to','be','alive!']
    String1 = " ".join(list1) 
    print(String1) # "What a time to be alive!"
    
    String2 = "-".join(list1)
    print(String2) # "What-a-time-to-be-alive!"
    ```
    
- 
- Dictionaries
- Tuples
- sets

# Tuple

- Tuples are used to store multiple items in a single variable.
- Tuple is one of 4 built-in data types in Python used to store collections of data
- A tuple is a collection which is ordered and immutable.
- Tuples are written with round brackets `()`.

```python
person_list = ["Sanjana", "India", 20]
person = ("Sanjana", "India", 20, 20)

print(person[0], person[2]) # "Sanjana" "India"

#person_list[0] = "Sneha"  ❌ because tuples are immutable
```

Lists and tuples are both similar to each other.  The only difference between them is list is mutable, whereas  tuples are immutable.

Due to the immutable nature of tuple there are several methods that are not supported by tuple but by list

| Methods | List support | Tuple support |
| --- | --- | --- |
| pop( ) | ✅ | ❌ |
| remove( ) | ✅ | ❌ |
| append( ) | ✅ | ❌ |
| insert( ) | ✅ | ❌ |

## Tuple Methods

- `count(x)` → returns the number of occurences of a element inside a tuple
- `index(x)` → return the index of the  given element if it is present inside a tuple. Otherwise, throws error

Here’s a demo of the  tuple methods.

```python
person_list = ["Sanjana", "India", 20]
person = ("Sanjana", "India", 20, 20)

print(person.count(20))  # 2
print(person.index("India"))  # 1
```

# Dictionaries in python

Dictionaries in python are similar to hashmap in anyother programming languages where the elements stored in form of ***key: value pairs.*** 

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

It means the keys in the dictionary should be unique.

```python
book = {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    }
```

## Dictionary Methods

| Methods | Description | Example | Output |
| --- | --- | --- | --- |
| get( key ) | it returns the value for the specified key | book.get(”title”) | “Infinite Jest” |
| keys( ) | it  returns a list of all the keys in the dictionary | book.keys( ) | [”title”, “rating”, “genre”] |
| values( ) | it returns a list of all the values in the dictionary | book.values( ) | [”Infinite Jest”, 4.5, “Fiction” ] |
| items( ) | it returns a tuple which has all the key: value  pairs of the dictionaries | book.items() | (
[('title', “Infinite Jest”), 
('rating', 4.5),
('genre', “Fiction”)]
) |

# Sets in Python

Sets in python are similar to sets in mathematics or the sets that we saw in SQL. 

Set has no order and no duplicates.

# Looping statements in Python

As usual in anyother programming languages, looping in python is used to repeat a set of steps in code. 

Using loops ensures, DRY principle

## While Loop in Python

While loop executes a set of code till the condition given to the loop is true. In otherwords, if condition became false, the execution  stops

### Syntax

```python
while(condition):
	statements
```

### Example

Given a number n make a pascal triangle with  ✨

```python
n = int(input())
i = 1
while i<=n:
    print('✨'*i)
    i+=1
```

## For-in loop in python:

The for in  loop is different from the typical for-loops that we’ve been using in other programming languages. 

This loop takes a loop-variable and a sequence. For each iteration it assigns loop-variable with each of the values in the sequence linearly.

### Syntax

```python
for i in range(6):
	#statements here
```

the `range()` function used here provides the sequence for the for-in loop.

### Syntax for `range()`

```python
range(<start>,<stop>,<step>) # similar to slicing operator
```

`NOTE`  For making code tidier, download black formatter  extension from marketplace. And, `ctrl` + `,` → settings → Enable  format on save