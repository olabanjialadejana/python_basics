femi = {}
femi["car"] = "toyota"
femi["fruit"] = "orange"

pair1 = input("enter pair 1\n")
pair2 = input("enter pair 2\n")


def add_to_femi(key, value):
    femi[key] = value


add_to_femi(pair1, pair2)


print(femi)
