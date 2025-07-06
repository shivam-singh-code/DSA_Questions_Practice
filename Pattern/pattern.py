# Pattern 1
def print_pattern1():
    for _ in range(5):
        for _ in range(5):
            print("#", end="")
        print("")

def print_pattern2():
    for i in range(5):
        for _ in range(i+1):
            print("#", end="")
        print("")

def print_pattern3():
    for i in range(5):
        for j in range(i+1):
            print(j+1, end="")
        print("")

def print_pattern4():
    for i in range(5):
        for _ in range(i+1):
            print(i+1, end="")
        print("")
    
def print_pattern5():
    for i in range(5):
        for j in range(5- i):
            print("#", end="")
        print("")
        
def print_pattern6():
    for i in range(5):
        for j in range(5 - i):
            print(j+1, end="")
        print("")
        
def print_pattern7():
    for i in range(5):
        # Print space
        for _ in range(5-i-1):
            print(" ", end="")
        
        # Print #
        for _ in range(2*i+1):
            print("#", end="")
            
        # Print space
        for _ in range(5-i-1):
            print(" ", end="")
        
        print("")

def print_pattern8():
    for i in range(5):
        # Print space
        for _ in range(i):
            print(" ", end="")
        
        # Print #
        for _ in range((2 * 5) - (2 * i + 1)):
            print("#",end="")
            
        # Print space
        for _ in range(i):
            print(" ", end="")
        
        print("")
        
def print_pattern10():
    
    n = 5
    for i in range((2 * n - 1) + 1):
        star_to_print = i
        if(i > n):
            star_to_print = 2 * n - i
        for _ in range(star_to_print):
            print("*", end="")

        print("")
        
print_pattern10()


# To Print Pattern 9 combine pattern 7 and 8