"""
Filename: n_fibonacci.py
Author: <Felix Olguin>
Created: <2/1/26>
Instructor: Holtslander
"""

def n_fibonacci():
    # Write your code here
    n = int(input("Please input a non-negative whole number.\n"))
    for i in range (n):
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        else:
            a = 0
            b = 1
            for i in range (2, i + 1):
                c = a + b
                a = b
                b = c
            print(c)               
            
            
# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("Print another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()