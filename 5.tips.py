print("# exchange two numbers # \n")
a = input("first num: ")
b = input("second num: ")
print("\n changing...\n")
message = "a = " + str(a) +", b = " + str(b) 
print(message)
a,b = b,a
message = "a = " + str(a) +", b = " + str(b)
print(message)

