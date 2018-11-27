def oneAway(s1, s2):
    if len(s1) == len(s2):
        oneEdit(s1, s2)
    if len(s1) == len(s2) - 1 or len(s1) == len(s2) + 1:
        oneCharacter(s1, s2)


def oneEdit(s1, s2):
    counter = 1
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            if counter == 0:
                return False
            else:
                counter -= 1
                i + +
    return True


def oneCharacter(s1, s2):
