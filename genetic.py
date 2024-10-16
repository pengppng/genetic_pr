# Function to compare loci sets and find who matches most closely with child by locus
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
        return "Both strings are identical.>>inclusive Be a family"
    elif diff_count == 1:
        return f"Check again diff 1 posi: Strings differ at position {diff_positions[0]}"
    elif diff_count == 2:
        return "Strings differ at 2 positions. Conclusion: Not the same."
    else:
        return "More than 2 differences found.>>exclusion \n They are not Family "

# Function to compare STR Locus between A and B
def compare_STR_locus(data_A, data_B):
    differences = []
    is_match = True

    # Iterate through each row
    for i, (locus_A, locus_B) in enumerate(zip(data_A, data_B)):
        locus_name = locus_A[0]  # The STR locus name
        alleles_A = locus_A[1:]  # Alleles for A
        alleles_B = locus_B[1:]  # Alleles for B

        # Compare if all alleles match
        if alleles_A != alleles_B:
            # If any alleles do not match, log the differences
            differences.append((locus_name, alleles_A, alleles_B))
            is_match = False

    # Summary
    if is_match:
        return "Both sets are identical. Conclusion: Yes"
    else:
        return f"STR Locus differences found: {differences}. Conclusion: No"

# Function to compare loci for SSR profiling
def compare_loci_by_locus(data, loci_names):
    # Compare two loci sets and count matching alleles
    def check_differences(child_loci, person_loci):
        return sum(1 for a, b in zip(child_loci, person_loci) if a == b)

    child = data['Child']

    # Summary for each locus comparison
    print("=== Detailed STR Profiling by Locus ===")
    for i, locus in enumerate(loci_names):
        print(f"\nLocus: {locus}")

        # Extract the loci values for the child and other individuals
        child_loci = child[i]  # Loci for the child
        comparisons = {}

        # Compare with Mother, Boyfriend, and Father
        for person in ['Mother', 'Boyfriend', 'Father']:
            person_loci = data[person][i]  # Loci for each person
            # Count how many values match with the child at this locus
            matches = check_differences(child_loci, person_loci)
            comparisons[person] = matches

        # Sort by who has the most matches with the child at this locus
        sorted_comparisons = sorted(comparisons.items(), key=lambda x: x[1], reverse=True)

        # Output results for this locus
        for person, matches in sorted_comparisons:
            print(f"{person} matches {matches}/2 alleles.")
        
        # Show the closest match for this locus
        print(f"Most likely match at {locus}: {sorted_comparisons[0][0]}")

    print("\n=== Summary Completed ===")

# Main function to allow user to select the function
def main():
    print("Select the function you want to use:")
    print("1. Check Mother-Child") #mtDNA
    print("2. Check Father-Child") #STR
    print("3. Who is the father of the child") #SSR profiling

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Compare mtDNA
        string1 = input("Enter the first mtDNA string: ")
        string2 = input("Enter the second mtDNA string: ")
        result = check_strings(string1, string2)
        print(result)

    elif choice == '2':
        # Compare STR Locus between A and B
        # Data from the image can be used or user input can be added here
        data_A = [
            ("D8S1179", 11, 16),
            ("D21S11", 29, 31.2),
            ("D7S820", 10, 11),
            ("CSF1PO", 12, 12),
            ("D3S1358", 15, 15),
            ("TH01", 7, 9),
            ("D13S317", 8, 12),
            ("D16S539", 9, 12),
            ("D2S1338", 18, 19),
            ("D19S433", 13, 14),
            ("vWA", 14, 17),
            ("TPOX", 8, 8),
            ("D18S51", 16, 24),
            ("Amelogenin", "X", "Y"),
            ("D5S818", 11, 12),
            ("FGA", 22, 22)
        ]

        data_B = [
            ("D8S1179", 11, 14),
            ("D21S11", 29, 32.2),
            ("D7S820", 8, 10),
            ("CSF1PO", 12, 12),
            ("D3S1358", 16, 16),
            ("TH01", 9, 9),
            ("D13S317", 8, 12),
            ("D16S539", 9, 11),
            ("D2S1338", 19, 21),
            ("D19S433", 14, 15.2),
            ("vWA", 16, 17),
            ("TPOX", 8, 8),
            ("D18S51", 15, 16),
            ("Amelogenin", "X", "Y"),
            ("D5S818", 10, 12),
            ("FGA", 20, 21)
        ]

        result = compare_STR_locus(data_A, data_B)
        print(result)

    elif choice == '3':
        # SSR Profiling
        data = {
            'Mother': [(21, 23), (8, 10), (12, 13), (14, 18), (10, 11), (13, 14), (31.2, 32.2), (6, 9), (16, 17), (11, 14), (8, 12), (11, 13), (9, 10), (11, 12), (7, 8)],
            'Child': [(22, 23), (8, 11), (12, 13), (14, 14), (11, 16), (14, 14), (30, 32.2), (6, 9.3), (16, 17), (11, 14), (8, 11), (9, 13), (8, 9), (12, 11), (11, 12)],
            'Boyfriend': [(21, 22), (11, 11), (13, 13), (17, 18), (10, 11), (14, 17), (30, 30), (5, 6), (15, 15), (11, 14), (8, 11), (9, 13), (8, 8), (7, 12), (11, 12)],
            'Father': [(20, 22), (11, 11), (13, 13), (14, 15), (14, 16), (14, 17), (29, 30), (6, 9.3), (15, 17), (11, 12), (12, 12), (9, 10), (8, 9), (10, 13), (11, 12)]
        }

        loci_names = [
            'FGA', 'TPOX', 'D8S1179', 'vWA', 'Penta E', 'D18S51', 
            'D21S11', 'TH01', 'D3S1358', 'Penta D', 'CSF1PO', 
            'D16S539', 'D7S820', 'D13S317', 'D5S818'
        ]

        compare_loci_by_locus(data, loci_names)

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Run the main function
main()
