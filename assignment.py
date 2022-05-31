# Category 1(a)
def upper(str):
    string = str.upper()
    return string


print(upper("the new line"))


def lower(str):
    string = str.lower()
    return string


print(lower("HELLO WORLD"))


# Category 1(b)
def numeric_values_in_string(value):
    for character in value:
        if character.isdigit():
            return True
    return False


print(numeric_values_in_string('1s4f6h'))


# Category 1(c)
def given_string_valid(str):
    if str.isdigit():

        return False
    else:

        return True


print(given_string_valid("90"))






