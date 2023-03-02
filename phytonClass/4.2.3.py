txt = int(input("Insert the temperature you would like to convert: "))
temperature = txt[-1:]
Upper_case = temperature.upper()
c = (5*txt-160)/9
f = (9*txt+(32*5))/5
if(Upper_case == F):
    print(c)
else:
    print(f)