def remove_numeric_value(str):
    alpha = ""
    for i in str:
        if not i.isdigit():
            alpha = alpha + i
    result = alpha.lower()
    result_1 = alpha.upper()
    print(result)


remove_numeric_value('ABCd1234efg567')