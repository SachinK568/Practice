name = input("Enter keyword = ")
name.lower()
vowels=0
constants=0

for n in name:
    if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
        vowels = vowels+1
    else:
        constants = constants + 1

print("No of vowels is",vowels)
print("No of constants is",constants)