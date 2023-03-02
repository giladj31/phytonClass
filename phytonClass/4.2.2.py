txt = str(input("Enter a word: "))
x = str(txt[::-1])
if(x==txt):
    print('OK')
else:
    print('NOT')