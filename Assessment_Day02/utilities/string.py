def remove_punctuation(s):
    result = ""
    punctuations = "!()-[]{};:'\",<>./?@#$%^&*_~"   
    for ch in s:
        if ch not in punctuations:  
            result += ch
    return result


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s.lower():  
        if ch in vowels:
            count += 1
    return count
