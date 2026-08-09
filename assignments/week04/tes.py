# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a,e,i,o,u)

# ตัวอย่างหน้าจอ
# What is your name? : Booncho
# Your text have 4 vowels.

name = input ("What is your name? :")
"""letters = list("Warintorn")
print (letters)

a = letters.count ('a')
e = letters.count ('e')
i = letters.count ('i')
o = letters.count ('o')
u = letters.count ('u')

A = letters.count ('A')
E = letters.count ('E')
I = letters.count ('I')
O = letters.count ('O')
U = letters.count ('U')
count = a + e + i + o + u + A + E + I+ O+ U """

count = 0
for letter in name: 
    if letter == 'a' or letter == 'A':
        count = count +1
    elif letter == 'e' or letter == 'E':
        conut = count +1
    elif letter == 'i' or letter == 'I':
        count = count +1
    elif letter == 'o' or letter == 'O':    
        count = count +1
    elif letter == 'u' or letter == 'U':
        count = count +1
        print(f" ตัวอักษร: { letter }")

print("Your text have " , count , "vowets")
    