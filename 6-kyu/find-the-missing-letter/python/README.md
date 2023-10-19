# Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

~~~if:factor
In the case of factor, your array of letters will be a string.
~~~

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.<br>
The array will always contain letters in only one case.

Example:
~~~if-not:swift,factor
```
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
```
~~~

~~~if:factor
```factor
"abcdf" -> CHAR: e
"OQRS" -> CHAR: P
```
~~~

```if:swift
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
```

(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have also created other katas. Take a look if you enjoyed this kata!