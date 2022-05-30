def kilograms_to_pound_and_vicevers(numb):
    kilogram_to_pound = numb * 2.20462

    print("result of pound is :", kilogram_to_pound)

    pound_to_kilo = numb * 0.453592
    print("result of kilogram is :", pound_to_kilo)


key = int(input('please enter your input : '))
kilograms_to_pound_and_vicevers(key)


def miligram_to_ounce_and_vicevers(numb):
    miligram_to_ounce = numb * 3.5274e-5

    print("result of ounce is :", miligram_to_ounce)

    ounce_to_miligram = numb * 28349.5

    print("result of miligram is :", ounce_to_miligram)


key = int(input('please enter your input : '))
miligram_to_ounce_and_vicevers(key)
