# Function to check differences between two strings for mtDNA
def check_strings(string1, string2):
    if len(string1) != len(string2):
        return "String lengths are not the same."

    diff_count = 0
    diff_positions = []

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diff_count += 1
            diff_positions.append(i)

    if diff_count == 0:
        return "Both strings are identical."
    elif diff_count == 1:
        return f"Check again: Strings differ at position {diff_positions[0]}"
    elif diff_count == 2:
        return "Strings differ at 2 positions. Conclusion: Not the same."
    else:
        return "More than 2 differences found."

# Function to compare number sets A, B, C check SSR profiling
def compare_numbers(set_a, set_b, set_c):
    def check_differences(set1, set2):
        diff_count = sum([1 for a, b in zip(set1, set2) if a != b])
        return diff_count

    # Compare A with B
    diff_ab = check_differences(set_a, set_b)
    
    if diff_ab == 1 or diff_ab == 2:
        print("A and B differ by 1-2 positions, need to check 3 times.")
        for _ in range(3):
            print("Rechecking...")
        return "A and B are similar."
    elif diff_ab >= 3:
        return "A and B have no relationship, recheck required."

    # Compare A with C
    diff_ac = check_differences(set_a, set_c)
    
    if diff_ac == 1 or diff_ac == 2:
        print("A and C differ by 1-2 positions, need to check 3 times.")
        for _ in range(3):
            print("Rechecking...")
        return "A and C are similar."
    elif diff_ac >= 3:
        return "A and C have no relationship, recheck required."

# Function to summarize results with input from user
def summarize_results():
    # รับ input จากผู้ใช้เป็น string 2 ชุด
    string1 = input("Enter the first string: ")  # รับ string1 จากผู้ใช้
    string2 = input("Enter the second string: ")  # รับ string2 จากผู้ใช้

    print("=== Part 1 ===")
    result_string = check_strings(string1, string2)
    print(result_string)

    # รับชุดข้อมูลตัวเลขจากผู้ใช้
    set_a = list(map(int, input("Enter set A (comma-separated numbers): ").split(',')))  # รับชุดข้อมูล A จากผู้ใช้
    set_b = list(map(int, input("Enter set B (comma-separated numbers): ").split(',')))  # รับชุดข้อมูล B จากผู้ใช้
    set_c = list(map(int, input("Enter set C (comma-separated numbers): ").split(',')))  # รับชุดข้อมูล C จากผู้ใช้

    print("=== Part 2 ===")
    result_numbers = compare_numbers(set_a, set_b, set_c)
    print(result_numbers)

    print("=== Summary ===")
    if "similar" in result_string.lower() and "similar" in result_numbers.lower():
        print("Both string and number comparisons indicate similarity.")
    else:
        print("Discrepancies found in string or number comparisons.")

# Call the function to run the program
summarize_results()


#how to run code type this "python genetic.py" in terminal
