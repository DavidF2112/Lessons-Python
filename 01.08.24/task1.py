def find_fragments(text):
    fragments = []
    length = len(text)
    
    i = 0
    while i < length - 2:
        if text[i].lower() == 'r' and text[i+1] == 'b':
            j = i + 1
            while j < length - 1 and text[j] == 'b':
                j += 1
            if j < length and text[j] == 'r':
                fragments.append(text[i:j+1])
                i = j  
            else:
                i += 1
        else:
            i += 1
    
    return fragments


text = "Rbbbr and rbr and Rbr and RBBBBBr and rbbr"
matches = find_fragments(text)
print(matches)
