import multiprocessing

def factorial(x):
    fact = 1
    if x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,x + 1):
            fact = fact*i
    print("The factorial of",x,"is",fact)
    
def fibonacci_series(n):
    fib_series = [0, 1]
    
    while len(fib_series) < n+1:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    print(fib_series)
    
def sort_n(arr):
    print("Ascending order array")
    sorted_numbers = sorted(arr)
    print(sorted_numbers)

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    if number == digit_sum:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
        
def is_palindrome(s):
    s1 = s.lower() 
    s2 = ''.join(char for char in s1 if char.isalnum())  
    if s1 == s2[::-1] : 
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
        
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")
        
def file_with_line_count(filename):
    try:
        with open(filename,'r') as fh:
            lines = fh.readlines()
            line_count = len(lines)
            print(f"Total lines in {filename}': {line_count}\n")
            for line_number, line in enumerate(lines, start=1):
                print(f"Line {line_number}: {line.strip()}")
                
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

def add_real_numbers(a, b):
    print(f"sum of {a} and {b} =",a + b)
    
def reverse_number(number):
    reversed_num = int(str(number)[::-1])
    print(f"The reverse of {number} is: {reversed_num}")
    
def convert_case(input_string):
    u_to_l = input_string.lower()
    l_to_u = input_string.upper()
    print(f"Original String: {input_string}")
    print(f"Uppercase to Lowercase: {u_to_l}")
    print(f"Lowercase to Uppercase: {l_to_u}")

#main driver code        
"""n = 10 
fib_series = fibonacci_series(n)


num = 153 
is_armstrong_number(num)

input_str = "A man, a plan, a canal, Panama!" 
result = is_palindrome(input_str)

num = 7 
check_even_odd(num)

f="OS.txt"
file_with_line_count(f)

num1 = float(input("Enter the first real number: "))
num2 = float(input("Enter the second real number: "))
sum_result = add_real_numbers(num1, num2)

num = 5678
reverse_number(num)

string_input = input("Enter a string: ")
convert_case(string_input)"""

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=factorial, args=(5, ))
    p2 = multiprocessing.Process(target=fibonacci_series, args=(9, ))
    p3 = multiprocessing.Process(target=sort_n, args=([5, 6, 2, 1, 8, 4], ))
    p4 = multiprocessing.Process(target=is_armstrong_number, args=(153, ))
    p5 = multiprocessing.Process(target=is_palindrome, args=("A man, a plan, a canal, Panama!", ))
    p6 = multiprocessing.Process(target=check_even_odd, args=(47, ))
    p7 = multiprocessing.Process(target=file_with_line_count, args=("OS.txt", ))
    p8 = multiprocessing.Process(target=add_real_numbers, args=(23,47))
    p9 = multiprocessing.Process(target=reverse_number, args=(56789, ))
    p10 = multiprocessing.Process(target=convert_case, args=("OPERATING SYSTEM", ))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
