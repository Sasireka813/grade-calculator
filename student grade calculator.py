name=input("Enter your name :")
Tamil=int(input("Enter your Tamil mark :"))
English=int(input("Enter your English mark :"))
Maths=int(input("Enter your Maths mark :"))
Science=int(input("Enter your Science mark :"))
SST=int(input("Enter your SST mark :"))
print("Student Name:",name)
Total=Tamil+English+Maths+Science+SST
print("Total mark",Total)
Average=Total/5
print("Average",round(Average))
if Average>=90 and Tamil>=35 and English>=35 and Maths>=35 and Science>=35 and SST>=35:
	print("Grade:A+")
elif Average>=80 and Tamil>=35 and English>=35 and Maths>=35 and Science>=35 and SST>=35:
	print("Grade:A")
elif Average>=70 and Tamil>=35 and English>=35 and Maths>=35 and Science>=35 and SST>=35:
	print("Grade:B")
elif Average>=60 and Tamil>=35 and English>=35 and Maths>=35 and Science>=35 and SST>=35:
	print("Grade:C")
else:
	print("Fail")
