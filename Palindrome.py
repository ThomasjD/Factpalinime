#Determine if a word is a palindrome

#word input
word = input("Enter a word.")
#w,o,r,d 1 to 4
drow = ""
for x in range(1, len(word) + 1):
    drow += word[-x]
drow= str(drow)

print (drow)

if drow == word:
    print (f"This {word} is a palindrome!!!")
    print (f"{word} == {drow}.")
else:
    print (f"{word} != {drow}.")
    print (f"This {word} is a not a palindrome!!!")
#odd words
#find index of middle letter
#divide by 2
#7/2 = 3.5 round that whole number down

#even words
#divide word by 2, then first letter of last = last letter of the other side
