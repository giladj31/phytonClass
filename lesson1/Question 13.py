Class1=int(input("The number of students in class 1 is:"))
Class2=int(input("The number of students in class 2 is:"))
Class3=int(input("The number of students in class 3 is:"))
Class4=int(input("The number of students in class 4 is:"))
sum=Class1+Class2+Class3+Class4
average=sum/4
StudentCost=45
print("The number of students participating in the activity is", sum)
print("The average of the students studying in each class is", average)
print("The cost of running the project is", StudentCost*sum)