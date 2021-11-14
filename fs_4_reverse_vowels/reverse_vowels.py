def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiou'
    temp =[]
    for letter in s:
        if letter.lower() in vowels:
            temp.append(letter)
    print('current vowels in string are:', temp)
    temp2 = []

    for letter in s:
        if letter.lower() in vowels:
            temp2.append(temp[-1])
            temp.pop(-1)
        else:
            temp2.append(letter)
    
    return "".join(temp2)
    