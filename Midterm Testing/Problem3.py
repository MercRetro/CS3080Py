def xor_with_seven_and_write_to_file():
  filename = "output.txt"

  # Open the file in write mode
  with open(filename, "w") as file:
      # Take a list of integers from the user
      user_input = input("Enter a list of integers separated by spaces: ")
      integers = user_input.split()

      results = []

      for item in integers:
          try:
              # Convert each input to an integer
              num = int(item)
              # XOR the integer with 7
              result = num ^ 7
              # Print the result
              print(result)
              # Write the result to the file
              file.write(f"{result}\n")
              results.append(result)
          except ValueError:
              print(f"Invalid input detected: {item}, skipping...")

  print(f"Results have been written to {filename}")

# Run the function
xor_with_seven_and_write_to_file()
