fraza = "Langa o cabana, stand pe o banca, un bacan a spus un banc bun."
cuv = "bacan"

def lit(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

fraza2 = [cuv.strip(",.") for cuv in fraza.split()]

for i in fraza2:
    if lit(cuv, i):
        print(i)
