import random

def my_decorator_example(func):
    def _wrapper():
        print("This executes before de function")
        func()
        print("This executes after the function")
    return _wrapper


@my_decorator_example
def sayHello():
    print("hello!")
    


def sumDecorator(func):
    def sumWrapper(*args,**kwargs):
        return func(*args,**kwargs) + func(*args,**kwargs)
    return sumWrapper 

@sumDecorator
def generateRandom():
    random_number = random.randint(1,9)
    print(random_number)
    return random_number
def generateString():
    return "awsd"

##########################################

def divide_decorator(func):
    def divide_wrapper(*args,**kwargs):
        if args[1] == 0:
            return None
        return func(*args,**kwargs)
    
    return divide_wrapper
        


@divide_decorator
def divide_numbers(a,b):
    return a/b

if __name__ == '__main__':
   print(divide_numbers(5,0))
   pass