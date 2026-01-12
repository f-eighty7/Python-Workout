def hex_output():
    decnum = 0
    hexnum = input("Enter a hexnumber to convert: ")

    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16**power)
    print(decnum)


# hex_output()