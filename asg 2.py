print("Question 1\n")

# giving value to sentence.
sentence = 'Python is a case sensitive language'

# printing the length of sentence.
print("\nPart a ")
print(f"Length of input = {len(sentence)}")

# printing the sentence in reverse order.
print("\nPart b")
print(sentence[::-1])


# slicing and printing the sentence.
print("\nPart c")
sliced_string =sentence[10:26]
print(sliced_string)
print


# replacing and printing.
print("\nPart d")
new_sentence = sentence.replace("a case sensitive", "object oriented")
print(new_sentence)


# printing index of "a" from sentence.
print("\nPart e")
print(sentence.index("a"))


# replacing blank white spaces with empty string.
print("\nPart f")
print(sentence.replace(" ", ""))


#######################################################

print("Question 2\n")

# Variables.
name = "Ramya"
SID = "21105016"
department name = "ECE"
CGPA = "9.9"

# Printing statements in the given format.
print(f"Hey, {name} here! \nMy SID is {SID} \nI am from {department name} and my CGPA is {CGPA}")


########################################################

print("Question 3\n")


a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


########################################################

print("Question 4\n")

# taking input of 3 numbers from the user.
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

#finding the highest no.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"Highest no. = {highest_number}")


##############################################################

print("Question 5\n")

# taking string from the user.
string = input("Enter string: ")

if "name" in string:
    print("Yes")
else:
    print("No")

#############################################################

print("Question 6\n")

# taking input of 3 lengths from the user.
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

# checking condition for triangle.
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")

##############################################################
