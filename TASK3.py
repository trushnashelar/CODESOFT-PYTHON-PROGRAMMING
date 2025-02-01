import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '?', '.', '<', '>', '/', ':', ';']

print("-----Password Generator-----")

n_let = int(input("No. of letters you want in password: "))

n_nos = int(input("No. of numbers you want in password: "))

n_symb = int(input("No. of symbols you want in password: "))

p_list = []

for i in range(1, n_let+1):
    a = random.choice(letters)
    p_list += a

for i in range(1, n_nos+1):
    b = random.choice(nos)
    p_list += b

for i in range(1, n_symb+1):
    c = random.choice(symb)
    p_list += c

random.shuffle(p_list)

password = ""

for i in p_list:
    password += i

print("Generated password is: ", password)
