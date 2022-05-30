def meters_to_feet_and_vicevers(numb):
    meter_to_feet = numb * 3.281
    print("result of meter is  : ", meter_to_feet)
    feet_to_meter = numb * 0.3048
    print("result of feet is :", feet_to_meter)


key = int(input('please enter your input : '))
meters_to_feet_and_vicevers(key)


def centimeter_to_inch_and_vicevers(numb):
    centi_to_inch = numb * 0.393701

    print("result of inch is :", centi_to_inch)

    inch_to_centi = numb * 2.54
    print("result of centimeter is :", inch_to_centi)


key = int(input('please enter your input : '))
centimeter_to_inch_and_vicevers(key)