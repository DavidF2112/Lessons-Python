text = input("Enter some text:: ")
slovar = {}
text_lis = text.split()
slovar[text] = len(text_lis)
print(slovar)