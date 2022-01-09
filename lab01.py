def display_current_value():
    print("Current Value:", current_value)

def add(to_add):
    global current_value, previous_value
    previous_value = current_value
    current_value += to_add

def subtract(to_sub):
    global current_value, previous_value
    previous_value = current_value
    current_value -= to_sub

def mult(to_mul):
    global current_value, previous_value
    previous_value = current_value
    current_value *= to_mul

def div(to_div):
    global current_value, previous_value
    previous_value = current_value
    if (to_div == 0):
        print("Error, division by zero.")
    else:
        current_value /= to_div

def memory():
    global current_value, saved_value
    saved_value = current_value

def recall():
    global current_value, saved_value
    current_value = saved_value

def undo():
    global current_value, previous_value 
    current_value, previous_value = previous_value, current_value

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    saved_value = 0
    previous_value = 0

    display_current_value()
    add(5)
    subtract(2)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    mult(10)
    display_current_value()
    undo()
    undo()
    display_current_value()
    undo()
    undo()
    undo()
    display_current_value()
    div(False)


