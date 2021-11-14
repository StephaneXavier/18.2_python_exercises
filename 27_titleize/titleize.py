def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result = []
    phrase_in_list_lower = phrase.lower().split(' ')
    
    for elem in phrase_in_list_lower:
        result.append(elem.capitalize())
    
    return " ".join(result)

