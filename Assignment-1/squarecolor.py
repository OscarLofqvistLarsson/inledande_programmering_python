x = input("Enter a position on the chessboard")

letter = x[0] 

number = int(x[1])

letter = ord(letter)

if ((letter + number) % 2 == 0):
    print("Black")

else:
    print("White")