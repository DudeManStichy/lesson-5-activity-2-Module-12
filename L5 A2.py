input("Left shift doubles, right shift halves. press Enter to continue...")
print(" 3 << 1 =", 3 << 1, " 12 >> 1 =", 12 >> 1)
print(" 3 << 2 =", 3 << 2, " 12 >> 2 =", 12 >> 2)

n = int(input("enter a number (try 5 or 8): "))
guess = input("What is " + str(n) + " << 2? ")
input("Left shift by 2 multiplies by 4. Press Enter to continue...")
print(" ", n, "<< 2 =", n << 2, " you guessed:", guess)