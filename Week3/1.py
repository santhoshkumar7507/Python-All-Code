year = int(input("When did India get its independence (year)? "))

while year != 1947:
    print("Come on, don't you know even this?")
    print("That's okay, I will let you attempt this once more.")
    
    # Prompt for input again inside the loop
    year = int(input("When did India get its independence? "))

    print("Hip Hip Hurray. You got that right!")