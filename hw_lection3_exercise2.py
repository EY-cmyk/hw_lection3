numb = input("Input number:")
if len(numb) > 10:
    print("Incorect len!")
elif len(numb) < 10:
    print("Incorect len!")
elif numb is str:
    print("Incorect int!")
else:
    print(numb)