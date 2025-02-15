
def check_valid_name(name):
    return name.isalpha()  # isalpha() check the name contain only string 
    

def check_number(number):
    return number.isdigit()


def check_email(email):
    return '@' in email
