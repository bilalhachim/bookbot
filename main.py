import string
def CountWords(text):
    return len(text.split())
def CountCharacters(text):
    count=0
    dict = {}
    for letter in string.ascii_lowercase:
        for xCharacter in text.lower():
            if(letter==xCharacter):
                count+=1  
            dict[letter]=count
        count=0  
    return dict

def PrintReport(dic,len):
    print("--- Begin report of books/frankenstein.txt ---",end='\n')
    print(f"{len} words found in the document",end ='\n')
    for key, value in dic.items():
        print(f"The '{key}' character was found {value} times", end ='\n')
    print("--- End report ---")
file = open("books/frankenstein.txt")
text = file.read()
PrintReport(CountCharacters(text),CountWords(text))



   