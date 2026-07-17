print("""Enter a Password:
      1.Should consist of 8 characters,
      2.Should conssit of Uppercase,
      3.Should consist of Lowercase,
      4.Should consist of Number,
      5.Should consist of symbols
      Based on this the strength, results will be displayed
      """)
password = input()
print(f"\nYour Password : {password}")

special_characters = "!@#$%^&*()-+?_=,<>/"

flag=0

if len(password) > 8: #Check for length
    flag+=1
    
for x in password:    #Check for uppercase
    if x.isupper():
        flag+=1
        break
    
for x in password:    #Check for Lowercase
    if x.islower():
        flag +=1
        break

for x in password:     #Check for digits
    if x.isdigit():
        flag +=1
        break

for x in password:     #Check for special Characters
    if x in special_characters:
        flag+=1
        break
    
if flag == 5:   #rating the password
    print("Password strength : HIGH")
elif flag >= 3:
    print("Password strength : Medium")
elif flag >= 1:
    print("Password strength : Low")
else:
    print("Please enter a password")