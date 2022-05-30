def hours_to_min_and_vicevers(numb):
    hours_to_min= numb * 60

    print("result of min is :", hours_to_min)

    min_to_hours = numb * 0.0166667
    print("result of hours is :", min_to_hours)


key = int(input('please enter your input : '))
hours_to_min_and_vicevers(key)


def min_to_sec_and_vicevers(numb):
    min_to_sec= numb * 60

    print("result of sec is :", min_to_sec)

    sec_to_min = numb * 0.0166667
    print("result of minute is :", sec_to_min)


key = int(input('please enter your input : '))
min_to_sec_and_vicevers(key)
