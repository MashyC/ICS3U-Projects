
#Asks for value, then the base the value is in, then finally the desired base
value = input("Enter Value: ")
base = int(input("Enter Current Base (max. base 16): "))
newBase = int(input("Enter New Base (max. base 16): "))

#Representation of how much each digit is equivalent to in Decimal
toDec = {
    "0" : 0,    "1" : 1,    "2" : 2,    "3" : 3,
    "4" : 4,    "5" : 5,    "6" : 6,    "7" : 7,
    "8" : 8,    "9" : 9,    "a" : 10,    "b" : 11,
    "c" : 12,    "d" : 13,    "e" : 14,    "f" : 15
}

#Representation of all the characters
charValues = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e",
    "f"
]

#Any base into decimal (This was the decevingly "simple" part, even though it still took a lotta thinking)
def baseToDec(base, value):
    decValue = 0
    for placeValue in range(1, len(value) + 1):
        #For each digit, the value will be converted to base10 using the key, then multiplied by the place value mulitplier
        decValue += toDec[value[len(value) - placeValue]] * base ** (placeValue - 1)
        print(decValue)
        print("-")
    return decValue

#Decimal into any base (This was like, 200 times harder than base --> decimal)
def decToBase(base, value):
    #this whole thing creates a list of decimal numbers with proper place values
    #before converting it into an acutal number
    #
    #example: 3499,  base10 --> base16
    #becomes: [13, 10, 11] with proper place values
    #becomes: "dab" in hexadecimal
    digits = []
    remainingAmount = value
    lastHPV = 0
    while remainingAmount > 0:
        mulitplier = 1
        highestPV = 0
        #Seeing what's the highest digit of the new base can fit into the value, and remembering how many times it was able to fit
        #Repeats until there is no more value left to fit
        while base ** (highestPV + 1) <= remainingAmount:
            highestPV += 1
        else:
            while (mulitplier + 1) * (base ** highestPV) <= remainingAmount:
                mulitplier += 1

        #Adds significant zeros for all placevalues skipped
        if lastHPV - highestPV > 1:
            for n in range(1, lastHPV - highestPV):
                digits.append(0)
        #Adds significant non-zero numbers
        digits.append(mulitplier)
        remainingAmount -= (base ** highestPV) * mulitplier
        #Adds significant zeros to the end
        print(highestPV, mulitplier, remainingAmount, base ** highestPV)
        if remainingAmount == 0:
            for n in range(0, highestPV):
                digits.append(0)
        lastHPV = highestPV

    #Changes list of decimal values with proper digit division into an actual number
    finalValue = ""
    for digit in digits:
        finalValue += charValues[digit]
    return finalValue

decimal = baseToDec(base, value)
newValue = decToBase(newBase, decimal)
print(newValue)


wait = input("Press any key to continue...")
