Card_valid = False
pin_correct = True

if Card_valid == True:
    print("Access card accepted")
    if pin_correct == True:
        print("Access granted")
    else:
        print("Incorrect pin")
else:
    print("Invalid access card")