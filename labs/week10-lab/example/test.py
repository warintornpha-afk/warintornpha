"""
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input ("Insert your text :")
char =  input ("Character to find :")
 
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")
"""
"""
password = "Warintorn"
lenght = len ( password)
word = password.split('@')
if len(word) > 1:
    left = word [0].isalnum()
    right = word [1].isalnum()
else:
    left = False;
    right = False;
if lenght >= 8 and len(word) == 2 and left and right:
   print ("Your passsword is strong!")
else:
    print ("You password is not strong!") 
"""