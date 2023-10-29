def my_sqrt(x):
    sqr = x**.5
    return sqr
if __name__ == "__main__":
    res = my_sqrt(25)
    print(res)
#Parta The result is returned but not printed, so there is nothing on the display

# sqr is a local variable so it's not accessible outside the function. Change it to res would work cuz it stores the value of sqr

def my_print_square(x):
    square = x**2
    print(square)
res = my_print_square(25)
print(res)
#my_print_square print it but not storing it. my_sqrt store the output but not printing it
#625
#none
#my_print_square only prints a value instead and the returning value is None since it doesn't return anything

#Q3


