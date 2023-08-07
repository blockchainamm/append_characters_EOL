
# Append character(s) to End Of Line in the file based on given condition

# User input prompt to enter input file name
input_file = input("Enter the name of input file with extention: ")

# User input prompt to enter output file name
output_file = input("Enter the name of output file with extention: ")

# open input file in read mode and assign to variable istr
with open(input_file, 'r') as istr:

    # open input file in write mode and assign to variable ostr
    with open(output_file, 'w') as ostr:

        # Loop through each line read from the input file
        for line in istr:

            # Check if the line is not empty
            if line.strip():
                # Remove all trailing characters at End of Line (EOL)
                line = line.rstrip('\n')
                # Extract the last character of the line
                lastChar = line[-1]
                
                # Check if last character of line is a number
                if lastChar.isnumeric():
                    # If last character of line is a number append a single \ to the line
                    line = line + '\\'

            # Write the line to the output file
            print(line, file=ostr)