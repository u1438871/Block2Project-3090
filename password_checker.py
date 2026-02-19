import string

def check_password():
    password = input("Enter the password: ")
    strength = 0
    notes = ''

    strength += characters_score(password)
    strength += length_score(password)
    if common_score(password) == 0:
        strength = 0
    else:
        strength += 1

    if strength == 0:
        notes = "Your password is a common password! :( Change ASAP!"
    elif strength < 3:
        notes = "Your password is weak! Change ASAP!"
    elif strength < 6:
        notes = "Your password is alright. You should consider changing it."
    elif strength < 11:
        notes = "Your password is good. But it could be better."
    elif strength >= 11:
        notes = "Your password is strong! Good job"

    print(f"Password Strength: {strength}")
    print(f"Notes: {notes}")

def characters_score(password):
    score = 0
    lower_count = 0
    upper_count = 0
    number_count = 0
    wspace_count = 0
    special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        score += 1
    if upper_count >= 1:
        score += 1
    if number_count >= 1:
        score += 1
    if wspace_count >= 1:
        score += 1
    if special_count >= 1:
        score += 1

    return score

def length_score(password):
    length = len(password)
    score = 0

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 18:
        score += 1
    if length > 25:
        score += 1

    return score

def common_score(password):

    common_pass = {"12345","123456","12345678","123456789","password","1234567890","skibidi","1234567","pakistan123",
    "assword","123456","1234qwer","123456789","12345678","12345","1234567890","password","1234567","Contraseña",
    "mustufaj","123456","123456789","12345","veronica","lorena","12345678","1234567","valentina","teckiss","follar",
    "123456","123456789","12345","maria","Contraseña","susana","silvia","graciela","monica","claudia","12345",
    "123456","susana","marta","margarita","Contraseña","123456789","12345678","virginia","rodolfo",}

    if password in common_pass:
        return 0

    return 1

def ask_password():
    choice = input("Do you want to change or enter another password? (y/n)")
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        print("Invalid. Please enter y/n")
        return ask_password()


if __name__ == '__main__':
    print('Welcome to the password strength checker!')
    check_password()
    while ask_password() == True:
        check_password()
    print("Thanks for checking!")