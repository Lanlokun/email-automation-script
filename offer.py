def sort_by_level(filename):
    beginners = []
    intermediates = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Get column headers from the first line of the file
        headers = lines[0].strip().split(',')

        # Find the indices of required columns
        first_name_idx = headers.index("What is your first name?")
        last_name_idx = headers.index("What is you last name?")
        email_idx = headers.index("What is the email address you can be reached on?")
        level_idx = headers.index("Which level of the training are you applying for ?")

        for line in lines[1:]:
            data = line.strip().split(',')

            # Check if the line has enough elements to avoid errors
            if len(data) >= 11:
                first_name = data[first_name_idx]
                last_name = data[last_name_idx]
                email = data[email_idx]
                level = data[level_idx].lower()
                if level == 'beginner':
                    beginners.append(f"{first_name},{last_name},{email}\n")
                elif level == 'intermediate' or level == 'intermidiate':
                    intermediates.append(f"{first_name},{last_name},{email}\n")
                else:
                    print(f"Warning: Unrecognized level '{level}' in line: {line}")
            else:
                print(f"Skipping improperly formatted line: {line}")

    return beginners, intermediates

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines(data)
    if len(data) > 0:
        print(f"Successfully wrote {len(data)} lines to {filename}")

# Replace 'data.txt' with the actual filename containing the data and headers as specified
beginners_list, intermediates_list = sort_by_level('offers.csv')

# Write first name, last name, and email to individual files
write_to_file('beginners.txt', beginners_list)
write_to_file('intermediates.txt', intermediates_list)
