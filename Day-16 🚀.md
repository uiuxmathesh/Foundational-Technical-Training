# Day-16 🚀

# Javascript Day-1 🗓️

Javascript is a popular scripting language which has much similarities to python

## Softwares Needed

For executing javascript files there’s no additional software neede except your browser.

- Just open whatever browser you have
- Right click and select “Inspect”. (Shortcut: `ctrl` + `shift` + `I`
- Click on the `console` tab.
- This place serves as the compiler as well as REPL for yout JS code.

Although, it is possible to eexecute the JS Code in browser REPL, we need a code editor for editing JS code. Some of the  popular code editors for JS are,

- VScode
- Sublime

## Datatypes in JS

- String
- Number
- Bigint
- Boolean
- Undefined
- Null
- Symbol
- Object

### Type Coercion

Type coercion is the JS way of saying typecasting.

[Type Casting in JavaScript](https://dev.to/catherineisonline/type-casting-in-javascript-10la)

A Guide to  introduce JS typecastin

### Object

Javascript objects are similar to pythons dictionary. Both are key-value pairs. Both does the same thing. Unlike anyother programming language that follows OOPS, Objects in Javascripts are not instsance of a class

### Accessing Properties of Objects

- The properties of Objects can be accessed in two ways.
    - Square Bracket Notation `[ ]`
    
    ```jsx
    let myObj = {
    		name: 'Mathesh'
    		age: 21
    }
    console.log(myObj['name'])
    ```
    
    - Dot Notation `.`
    
    ```jsx
    let myObj = {
    		name: 'Mathesh'
    		age: 21
    }
    console.log(myObj.name)
    ```
    

## Template Literals

Template literals are same thing as Python’s `f'string'` .  Its got introduced in JS on ES2015

```jsx
//Noraml String

welcomeMsg = 'Hi ' + firstname + " ,Good morning 🌄"

//Template literal
welcomeeMsg = `Hi ${firstname}, Good morning`
```

## Declaring Variables in JS

Variables in Javascript like python doesn’t have any datatypes. So no need to specify datatypes at the time of variable creation. But there are three keywords used to declare variables in JS

`var` : classic JS way

`let` : From ES6

`const` : From ES6

### Comparison between `var` .`let` and `const`

| Keyword | Redeclaration | Reassignment |
| --- | --- | --- |
| var | ✅ | ✅ |
| let | ❌ | ✅ |
| const | ❌ | ❌ |

## Tasks in Javascript

**Task 1: Understand the following function and rewrite it using template literal**

```jsx
function movieUrl(domain, genre, year) {
    return "http://" + domain + "?genere=" + genre + "&year=" + year
}
```

Rewriting the above function in `template literal` 

```jsx
function movieUrl2(domain, genre, year) {
    return `https://${domain}?genre=${genre}&year=${year}`
}
```

## Destructuring of Arrays

```jsx
const [t1,t2] = [100,200]
console.log(t1,t2) // 100, 200
```

This line of code destructures the array on the right hand side of the `=` operator and assigns it to the left hand side of the operator

> **Note**:
> 
> 
> When in destructuring if there’s not enough values to destructure, then JS assigns undefined to the remaining values
> 
> ```jsx
> const [t1,t2,t2] = [100, 200]
> console.log(t1,t2,t3) // 100, 200, undefined
> ```
> 

We can also set default values for items in destructuring if it is going to be undefined

```jsx
const[t1, t2, t3=80] = [100,200]
console.log(t1,t2,t3) // 100, 200, 80
```

### Creating holes in destructuring

We can escape the values form the destructured format by creating holes

```jsx
const[, t1, t2, t3] = [100, 200, 300, 400]
console.log(t1,t2,t3) // 200, 300, 400
```

> When we declare a variable without assigning it belongs to type `undefined` . If you use `typeof()` function you will get undefined but in a string format. This is because the `typeof()` operator in JS returns always a ‘string’ type
> 

### Having too many values to unpack

```jsx
const[t1,t2,t3] = [100,200,300,400,500,600,700,800]
console.log(t1, t2, t3) //100, 200, 300 All other values will be exhausted and not used
```

## Rest operator & Spread Operator

### Rest

- Let’s say in the event of having too many values for destructuring, and  your do not want the rest of the values to get exhausted or wasted we can use rest operator `...`
    
    ```jsx
    const [t1, t2, ...t3] = [100, 200, 300, 400, 500, 600, 700, 800]
    console.log(t1, t2, t3) //100, 200, [300, 400, 500, 600, 700, 800] 
    ```
    
- One side note here is unlike python where we can use the unpacking operator `*` wherever in the argument list, the JS Rest operator should be only applied to only last element of the argument list.

### Spread

- Let’s say we have a array containing four elements, and we want to assign it to four different variables  in JS. We can do so by using spread operator `...`
    
    ```jsx
    const t1 = [100, 200, 300, 400]
    const [a, b, c, d] = ...t1
    console.log(a, b, c, d) //100, 200, 300, 400
    ```
    

## For Loops in JS

There are three types of for loops in JS

1. Typical for loop
2. For in loop
3. For of loop

Typical For loop

```jsx
console.log("Normal for loop");
for (let i = 0; i < marks.length; i++) {
  console.log(marks[i]);
}
```

For In Loop

```jsx
console.log("for...in");
for (let idx in marks) {
  console.log(marks[idx]);
}
```

For Of Loop

```jsx
console.log("for...of"); // for...in (python)
for (let mark of marks) {
  console.log(mark);
}
```

When to use which loop?

Usually in the order we learn the top one have the higher control and the last one have the higher convenience. It is preferred to use For-of loops for iterating over objects

## Double vs Triple equality operator

In JS the equality comparison operator is of two types. 

1. **Double (Loose) Equality operator `==`**
    
    It checks if the operands in both sides are equal. Doesn’t care about datatypes
    
    ```jsx
    a = 10
    b = '10'
    
    console.log(a==b) // True
    ```
    
2. **Triple (strict) equality operator `===`**
    
    It cheks the value as well as the datatype of the operator. (The usual ones in other programming languages)
    
    ```jsx
    a = 10
    b = '10'
    
    console.log(a===b) // False
    ```
    
    ## Event-Handling in Javascript
    
    Events are signals fired inside the browser window that notify of changes in the browser or operating system environment. Programmers can create *event handler* code that will run when an event fires, allowing web pages to respond appropriately to change.
    
    [Event handling (overview) - Event reference | MDN](https://developer.mozilla.org/en-US/docs/Web/Events/Event_handlers)
    
    Event-Handling in JS