def drink_coffee():
    global current_time, last_coffee_time, last_coffee_time2,too_much_coffee
    if current_time-last_coffee_time2 <=120:
        too_much_coffee = True
    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time

def display_knols():
    global knols
    print(knols)
def study(minutes):
    global knols, current_time, last_coffee_time, last_coffee_time2,current_time
    if last_coffee_time == current_time and not too_much_coffee:
        knols += 10*minutes
    elif last_coffee_time == current_time and too_much_coffee:
        pass
    else:
        knols += 5*minutes
    current_time += minutes
#The following initialize function is given
def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100
initialize()
if __name__ == "__main__":
    initialize() # start the simulation
    display_knols()
    study(60) # knols = 300
    display_knols()
    study(20) # knols = 400
    display_knols()
    drink_coffee() # knols = 400
    display_knols()
    study(10) # knols = 500
    display_knols()
    drink_coffee() # knols = 500
    display_knols()
    study(10) # knols = 600
    display_knols()
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    display_knols()
    study(10) # knols = 600
    display_knols()
