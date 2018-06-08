

def add_leading_zeros(num, strGoalLength):

    zeros = strGoalLength - len(str(num))
    leadingZeros = "0" * zeros
    return leadingZeros + str(num)
