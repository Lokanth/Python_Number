#This is a idea to make a Program to check the number sequence of findin number giviving
#if the sum of two number is equal to multiplication of that number then the programm will retur true or it will return false

#The First Step to Ask for range

NumberRange = int(input("Enter a Number:-"))

#In Order to make the Program Simple we only take number from 0 to 10
#In the next step we will check whether the number is grater than 0 and less than or equal to 10
sum = 0
mul = 1
NumberRange = NumberRange + 1
def count() :
	if NumberRange > 0 and NumberRange <= 110 :
	#From Hear The Next Step is to create a loop in which two number get added and multiplied and check if that they match together or not.
		for i in range(NumberRange) :
			for j in range(NumberRange) :
				for k in range(NumberRange) : 
					sum = i + j + k
					mul = i * j * k
					if sum == mul :
						print(mul)
	else :
		print("Number need to be modified")
def test() : 
	for i in range(10) :
		print(i)
count()
#test()
