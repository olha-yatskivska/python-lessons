import re

file_name = input("Enter log file name: ")
try:
    fhandle = open(file_name)
except:
    print("File could not be opened.")
    quit()

# Dictionary to store counts: { '404': 5, '500': 2 }
error_counts = dict()

for line in fhandle:
    line = line.rstrip()
    # Matches 4xx and 5xx codes (3-digit numbers starting with 4 or 5)
    # \b ensures we match the whole number only
    codes = re.findall(r'\b[45][0-9]{2}\b', line)
    
    for code in codes:
        # If code is not in dict, start at 0 and add 1
        error_counts[code] = error_counts.get(code, 0) + 1

fhandle.close()

# Analysis Output
print("\n--- Error Code Summary ---")
for code, count in sorted(error_counts.items()):
    print(f"Error {code}: {count} occurrences")

# Save summary to report
with open("error_report.txt", "w") as report:
    report.write("Log Error Analysis\n")
    for code, count in sorted(error_counts.items()):
        report.write(f"Code {code}: {count}\n")
