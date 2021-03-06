def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # d = {letter.lower():0 for letter in phrase if letter in ['a','e','o','i','u']}
    d= {}
    
    for letter in phrase:
        if letter in ['a','e','o','i','u']:
            d[letter.lower()] = d.get(letter.lower(),0) +1
    return d