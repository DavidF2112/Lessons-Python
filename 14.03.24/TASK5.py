text1 = input("Enter some text:: ").lower()
text2 = input("Enter some text:: ").lower()

text1 = text1.split()
text2 = text2.split()

max_len = 0 
max_len_for_a = 0 



for i in text1:
    if len(i) > max_len:
        max_len = len(i)
    for a in text2:
        if len(a) > max_len_for_a:
            max_len_for_a = len(a)
            if max_len_for_a == max_len:
                print("MAX LENGHT: ",max_len)
                break
