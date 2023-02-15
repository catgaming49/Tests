

#The decorator hijacks the original function in a way

#This function requires atleast one argument and the parameter is passed as the decorated function yayy
#After that you need a second function to handle the input so it needs to return a function that will be ran and the output is given printed
#This allow you to modify the original fucntion in several ways
def decorator(func):
    def wrap():
        toReturn = func() + " World!"
        return toReturn

    return wrap
    

#This decorator calls the function that is declared and gives it the function
def originalFunc():
    return "Hello,"

print(originalFunc()) # Return only Hello,

@decorator
def originalFunc(): # Because of the decorator this function return Hello, World!
    return "Hello,"

print(originalFunc())





