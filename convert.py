number = input("Enter the number you want to convert :")
number_system = {
    1: "unit",
    2: "ten",
    3: "hundred",
    4: "thousand",
    5: "tens of thousands",
    6: "hundreds of thousands",
}

units_and_tens = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eigteen",
    19: "Nineteen",
}

tens = {
    2: "Twenty",
    3: "Thirty",
    4: "Fourty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}

number_length = len(number)

if(number_length == 1 or number_length == 2) and (int(number) < 20):
    if(number == '0'):
        print(units_and_tens.get(0))
    else:
        print(units_and_tens.get(int(number)))

if(number_length == 2): 
    if(number[1] == '0'):
        print(tens.get(int(number[0])))
    else:
        print(tens.get(int(number[0])) + " " + units_and_tens.get(int(number[1])))