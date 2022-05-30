
# Category 1(a)
def upper(str):
    string = str.upper()
    return string


print(upper("the new line"))


def lower(str):
    string = str.lower()
    return string


print(lower("the new line"))

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
        print("User input is an Integer ")
    else:
        print("User input is string ")

given_string_valid("90")
