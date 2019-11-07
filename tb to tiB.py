size = int(input("enter size "))
symbol = input("enter symbol ")

powers = [2**10, 2**20, 2**30, 2**40, 2**50, 2**60, 2**70, 2**80]
if symbol == "T":
    converted = size / powers[3]
    print("You only have ", size / powers[3], "TiB")
    
elif symbol == "G":
    converted = size / powers[2]
    print("You only have ", size / powers[2], "GiB")

elif symbol == "M":
    converted = size / powers[1]
    print("You only have ", size / powers[1], "MiB")
elif symbol == "K":
    
    print("You only have ", size / powers[0], "KiB")

elif symbol == "P":
    
    print("You only have ", size / powers[4], "PiB")

elif symbol == "E":
    
    print("You only have ", size / powers[5], "EiB")

elif symbol == "Z":
    
    print("You only have ", size / powers[6], "ZiB")
