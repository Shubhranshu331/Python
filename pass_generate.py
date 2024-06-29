import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
n_letters=int(input("Enter the number of letters: "))
n_numbers=int(input("Enter the number of numbers: "))
n_symbols=int(input("Enter the number of symbols: "))

pass_list=[]
for char in range (1,n_letters+1):
    pass_list.append(random.choice(letters))
for char in range (1,n_numbers+1):
    pass_list += random.choice(numbers)
for char in range (1,n_symbols+1):
    pass_list += random.choice(symbols)


print(pass_list)
random.shuffle(pass_list)
print(pass_list)
password=""
for char in pass_list:
    password+=char
print(f"password generated is : {password}")
