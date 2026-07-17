
print("Enter a message")
m = input()

print("\nMessage : ", m)


ky=[]
for x in m:
    ky.append(ord(x))

enc=[]
for x in ky:
    enc.append(x+12)

print("\nEncrypted Text :")
for a in enc:
    print(chr(a),end="")

dec=[]
for x in enc:
    dec.append(x-12)

print("\nDecrypted text :")
for a in dec:
    print(chr(a),end="")   

    
