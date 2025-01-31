category = {
    "س": "S",
    "ث": "S",
    "ص": "S",
    "ش": "S",
    "ز": "Z",
    "ژ": "Z",
    "ظ": "Z",
    "ذ": "Z",
    "ض": "Z",
    "ت": "T",
    "ط": "T",
    "غ": "Q",
    "ق": "Q",
    "خ": "K",
    "ک": "K",
    "گ": "K",
    "ر": "R",
    "د": "D",
    "ج": "J",
    "چ": "J",
    "ل": "L",
    "ف": "F",
    "ح": "H",
    "ه": "H",
    "ب": "B",
    "پ": "B",
    "و": "V",
    "ن": "N",
    "ی": "Y",
    "ا": "A",
    "آ": "A",
    "ع": "A",
    "م": "M",  
}

code_category = {
    "س": "1",
    "ث": "1",
    "ص": "1",
    "ش": "1",
    "ز": "1",
    "ژ": "9",
    "ظ": "1",
    "ذ": "1",
    "ض": "1",
    "ت": "2",
    "ط": "2",
    "غ": "3",
    "ق": "3",
    "خ": "3",
    "ک": "9",
    "گ": "9",
    "ر": "4",
    "د": "2",
    "ج": "5",
    "چ": "5",
    "ل": "4",
    "ف": "6",
    "ح": "7",
    "ه": "7",
    "ب": "8",
    "پ": "8",
    "و": "6",
    "ن": "9",
    "ی": "9",
    "ا": "9",
    "آ": "9",
    "ع": "9",
    "م": "9",  
}

def soundex(word):
    soundex_code = category[word[0]]
    for i in range(1, len(word)):
        soundex_code += code_category[word[i]]
        
    return soundex_code

def query_soundex(input):
    words = input.split(' ')
    soundex_codes = []
    for word in words:
        soundex_codes.append(soundex(word))
    
    return soundex_codes