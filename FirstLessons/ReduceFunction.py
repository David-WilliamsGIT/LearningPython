# reduce() function applies the reduction function to an iterable object and reduce it to a single value

# reduce(function, iterable)

import functools
letters = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]

word = functools.reduce(lambda x,y,:x + y, letters)

print(word)

factorial = [5, 4, 3, 2, 1]

result = functools.reduce(lambda x,y,:x * y, factorial)
print(result)