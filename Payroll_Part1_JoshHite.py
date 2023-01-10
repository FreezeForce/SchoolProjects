#Employee Name Input
ename = input("Please enter your name: ")

#Tax Rate
Tax = .20

#Hours Worked
hwork = (int(input("Please enter your hours worked: ")))

#Pay Rate
PR = (int(input("Please enter your hourly rate: ")))

#Pay rate * hours worked
PRHW = hwork*PR

#Calculations for gross pay taxes
GPT =(hwork*PR)*Tax

#Net pay
NP =(hwork*PR)-GPT

#Output
print(ename)
print("Worked " + str(hwork) + " hours this period")
print("paid $" + str(GPT) + " in taxes")
print("He/She had a net pay of $" + str(NP))
