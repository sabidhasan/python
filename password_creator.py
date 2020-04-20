def validate():
    import re
    while True:
        password_creation = input(str("Enter a password: "))
        if len(password_creation) < 8:
            print("Make sure your password is at lest 8 characters. ")
        elif re.search('[0-9]', password_creation) is None:
            print("Make sure your password contains a number. ")
        elif re.search('[A-Z]', password_creation) is None:
            print("Make sure your password contains an upper case letter. ")
        elif re.search('[a-z]', password_creation) is None:
            print("Make sure your password contains a lower case letter. ")
        elif re.search('[!£$_=+\'?><,.{}\[\]%|`¬^&*@~#\"]', password_creation) is None:
            print("Make sure your password contains a special character. ")
        else:
            print("Password valid. ")
            break
    password_confirmation = input(str("Confirm your password by re-entering it. "))
    if password_confirmation == password_creation:
        print("Password confirmation completed. "
              "We have successfully created an account."
              "You must now log in to access your account. ")
    else:
        password_confirmation = False
        print("Error. Your password doesn't match the password you entered above.")
        return


validate()