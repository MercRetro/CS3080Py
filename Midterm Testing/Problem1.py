def get_input():
    try:
        input1 = input("Enter a string: ")
        if not isinstance(input1, str):
            raise ValueError

        input2 = int(input("Enter an integer: "))
        input3 = input("Enter another string: ")
        if not isinstance(input3, str):
            raise ValueError

        input4 = float(input("Enter a float: "))
        input5 = float(input("Enter another float: "))

        print("Inputs received:")
        print(f"String 1: {input1}")
        print(f"Integer: {input2}")
        print(f"String 2: {input3}")
        print(f"Float 1: {input4}")
        print(f"Float 2: {input5}")

    except ValueError:
        print("Incorrect input detected")

get_input()
