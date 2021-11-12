def cipher(text, shift, encrypt=True):

    """
    This function can shift letter by a defined units in a text.
    
    Parameters
    ----------
    text : str
        A string of text.
    shift : int
        Units of how the letter is shifted to the left(-) or right(+).
    encrypt : bool
        Default is True for encryption.
        
    Returns
    -------
    str
        The encrypted or decrypted string.
        
    Examples
    --------
    >>> cipher("hi", 1)
    'ij'
    """ 
 
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text