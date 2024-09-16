# lambda function (anonymous function)

def add(a, b):
    return a + b  

print(add(3, 4))  

def add(a, b):
    c=a+b
    print(c)

add(3,4)

def div(a,b):
    return a/b

div2=lambda a,b : a/b
print(div2(8,4))
    
multiply=lambda a,b:a*b
print(multiply(2,3))

'''lambda function do not contain any name it is a anonymous function we can see when we print div2 and div'''
print(div)
print(div2)


'''lambda expression practice'''

def is_even(a):
    return a%2==0    #a%2==0---->true false
    
print(is_even(5))

is_even=lambda a:  a%2==0 
print (is_even(8))

def last_char(s):
    return s[-1]

print (last_char('astha'))

last_char =lambda s: s[-1]
print(last_char('bhardwaj'))

# lambda with if , else

def func(s):
    if len(s)>5:
        return True
    return False

print(func('astha'))

func2 =lambda s: True if len(s)>5 else False
print(func2('abcdef'))

#above code can also be written like this

func2 =lambda s: len(s)>5 
print(func2('abcdef'))