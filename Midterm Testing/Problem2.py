def collect_inputs():
    inputs = []
    end_marker = "END"

    user_input = ""
    while user_input != end_marker:
        user_input = input("Enter a value (or type 'END' to stop): ")
        if user_input != end_marker:
            inputs.append(user_input)

    print("You entered the following values:")
    print(inputs)

collect_inputs()
