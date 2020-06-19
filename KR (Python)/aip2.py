s1 = "emerit"
s2 = "treime"

def anagram():
    global s1, s2

    for i in s1:
        if i not in s2:
            return False
        else:
            s2 = s2.replace(i, '', 1)
    if s2:
        return False
    return True

print(anagram())
print(s2, s1)