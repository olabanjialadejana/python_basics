def format_name(f_name, l_name):
    """This function takes in a first name and last name, and returns the names formatted in title case"""
    if f_name == "" or l_name == "":
        return "Mistake"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Result: {formated_f_name} {formated_l_name}'


print(format_name(input("What is your first name? "),
      input("What is your last name? ")))
