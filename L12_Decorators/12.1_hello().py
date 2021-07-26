def func():
    return 1
print(func())#1

def hello():
    return "Hello"
print(hello())#Hello
print(type(hello))#<class 'function'>

greet = hello
print(type(greet))
print(greet())#Hello

