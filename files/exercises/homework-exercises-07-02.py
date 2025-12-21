#Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
#Count these lines and then compute the total of the spam confidence values from these lines.
#When you reach the end of the file, print out the average spam confidence.
#Enter the file name: mbox.txt
#Average spam confidence: 0.894128046745

#Enter the file name: mbox-short.txt
#Average spam confidence: 0.750718518519

fname = input("Enter file name:")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line_s = line.rstrip()
        value = line_s[20:27]
        count = count + 1
        f_value = float(value)
        total = total + f_value    
print("Average spam confidence:",total/count)
