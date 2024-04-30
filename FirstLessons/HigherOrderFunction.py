# higher order function = a function that can either accept a function as an arguement or
# returns a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def Hello(func):
    text = func("Hello")
    print(text)
    
Hello(loud)
Hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))