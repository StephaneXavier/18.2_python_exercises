def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = []
    for char in phrase:
        if char.lower() != to_swap.lower():
            result.append(char)
        else:
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char.upper())
    return "".join(result)
               
        
            