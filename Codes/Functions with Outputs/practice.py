# l_name = input("what is your last name?:")
# f_name = input("what is your first name?:")


def format_name(l_name, f_name):
    if l_name == "" or f_name == "":
        return "No valid inputs provided"

    full_name = l_name.title() + ' ' + f_name.title()
    return f"Your full name is {full_name}"


print(format_name(input("what is your first name"), input("what is your last name")))
