Class=int(input("What is the number of students in the class? "))
Group=int(input("How many students in each group ?"))
print("Were accepted", Class//Group, "groups")
print("There is no group for", Class%Group, "pupils")