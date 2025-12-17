hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r= float(rate)
except:
    print("Error,please enter numeric input")
    quit()
     
print(h,r)
if h <=40:
    pay=h*r 
else:
    pay=40*r+(h-40)*r*1.5
print("Pay:",pay)
