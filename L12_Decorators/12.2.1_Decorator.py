
#Example(1)
#note: define greet() & welcome() inside hello and executed them inside hello() as well
#note: 方法A中包另外兩個方法 greet() & welcome()，這兩個方法只能在hello() 底下執行，無法單獨在外面呼叫
def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the great() func inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print("This is the end of the hello function")

hello()
#welcome() #無法執行 NameError: name 'welcome' is not defined
#greet() #無法執行 NameError: name 'greet' is not defined

# The hello() function has been executed
#          This is the great() func inside hello
#          This is welcome() inside hello
# This is the end of the hello function
print("-------------------------------------------------------------")

#Example(2)
#透過傳入的參數，來決定方法A內要執行哪個B方法
def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the great() func inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print("I am going to return function")

    if name == 'Jose':
        return greet
    else:
        return welcome

#note: 回傳 greet() function
my_new_func = hello("Jose")
# The hello() function has been executed
# I am going to return function

#note: 回傳 welcome() function，因為你沒有傳入(name='Jose')
print(my_new_func()) #This is the great() func inside hello


print("-------------------------------------------------------------")

#Example(3)
# 方法A中包另一個方法，並回傳另一個方法B   return a function with a function
def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()
print(some_func)#<function cool.<locals>.super_cool at 0x0000027A5EB80C10>
print(some_func())#I am very cool!


print("-------------------------------------------------------------")
#Example(4)
#透過傳入參數，將方法B當做參數傳入另一個方法A，並執行
##pass in a function into another function

def hello():
    return "Hi Jose!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

other(hello)#注意是寫hello，不是hello()!但執行的部分在print(some_def_func())會去執行hello()

# Other code runs here!
# Hi Jose!

print("-------------------------------------------------------------")
#Example(5)
#把要裝飾的function當作參數傳入A方法中，A方法中又包了B方法，B方法內包含傳入的參數和其他要增加的內容
#注意傳入時不要加()
def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code,after the original function")
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()#I want to be decorated!

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

# Some extra code, before the original function
# I want to be decorated!
# Some extra code,after the original function

print("-------------------------------------------------------------")

#承上
#上面那串def new_decorator() function可以用@new_decorator來表示
#代表你要把func_needs_decoratort傳入，加上一些裝飾(ex:額外的code)，最後再返回
#不需要把你的funtion裝飾的話，可以把@new_decorator註解掉


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()

# Some extra code, before the original function
# I want to be decorated!
# Some extra code,after the original function



# decorator 說明
# this key word of a new decorator.
# When you put it on top of function, it just says, OK, I'm going to pass this function.
# Into this as the original function, I'm going to do something to it, add some extra character,
# add some extra code  efore or after it calls the original function,
# wrap that into a nice function and then return that wrapped version.
# That's all the decorators doing here.
# It's essentially wrapping it around.


# Realistically you really won't be having to do this sort of coating of a new decorator, of the wrapping function, et cetera.

# Well, you will be doing is you're going to be using a Web framework or someone else's library and just
# adding in these new decorators to maybe render a new website or point to another page.

# So they're really commonly used in web frameworks such as Gengel or Flask, which is why it's important
# to understand behind the scenes what the decorator is actually doing.