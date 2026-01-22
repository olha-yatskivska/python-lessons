import re

# 1. File Opening Phase
file_name = input("Enter file name: ")
try:
    fhandle = open(file_name)
except:
    print(f"Error: File '{file_name}' cannot be opened.")
    quit()

num_list = list()

# 2. Extraction Phase (Extracting ALL numbers from each line)
for line in fhandle:
    line = line.rstrip()
    # re.findall returns a list of all matching strings
    # [0-9]+ matches one or more consecutive digits
    found_numbers = re.findall('[0-9]+', line)
    
    # 3. Processing and Filtering Phase
    for item in found_numbers:
        number = int(item)
        
        # Applying a filter (e.g., only numbers greater than 100)
        # In testing, this helps isolate high-priority data points
        if number > 100:
            num_list.append(number)

fhandle.close()

# 4. Analysis and Reporting Phase
if len(num_list) > 0:
    count = len(num_list)
    total_sum = sum(num_list)
    average = total_sum / count
    
    # Display results to the console
    print(f"\n--- Analysis Results ---")
    print(f"Total count (values > 100): {count}")
    print(f"Average value: {average:.2f}")

    # 5. Exporting results to an external report file
    with open("analysis_report.txt", "w") as report:
        report.write("AUTOMATED TEST DATA ANALYSIS REPORT\n")
        report.write("====================================\n")
        report.write(f"Source File: {file_name}\n")
        report.write(f"Total entries found: {count}\n")
        report.write(f"Sum of values: {total_sum}\n")
        report.write(f"Average: {average:.2f}\n")
        report.write("====================================\n")
    
    print("\nSuccess: Report has been saved to 'analysis_report.txt'")
else:
    print("No numbers matching the criteria were found in the file.")
