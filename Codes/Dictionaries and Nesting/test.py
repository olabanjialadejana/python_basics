student_scores = {
    "AYOOLA E.O.": 62,
    "ADEWOLE D.": 55,
    "ADEYEMI O.J.": 64,
    "AGBETUYI M.O": 61,
    "BAMIROLA E.J.": 68,
    "FRITZ I.G": 60,
    "OLAIYA O.I.": 45,
    "OSUNDARE T.J": 61,
    "OYEBISI A.I": 60,
    "SERIKI E.M.": 64,
    "ABASS": 67,
    "ABUBAKAR": 73,
    "ADE-EMMANUEL": 65,
    "ADEBISI O.A.": 62,
    "ADEBO": 50,
    "ADEBOWALE": 62,
    "ADEFILA": 64,
    "ADEGBITE": 66,
}

all_scores = []
for score in student_scores.values():
    all_scores.append(score)

highest = max(all_scores)

print(highest)
