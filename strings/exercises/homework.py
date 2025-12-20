#The numerical confidence score (in the context of X-DSPAM-Confidence) is measured in the range from 0.0 to 1.0. 
#Can we simply consider the value 0.8475 in this case as a decimal point followed by digits within the known range of [0.0 to 1.0] 

text = "X-DSPAM-Confidence:    0.8475"
num  = text.find('.')
dspam = text[num-1 : num+10]
print(float(dspam))
 

#p.s. num+10 - taking 10 since we know it'll be cutting at the end. 



text = "X-DSPAM-Confidence:    0.8475"
ipos  = text.find(':')
print(ipos)
piece = text.[ipos+1:]
print(piece)
value = float(piece)
print(value)
