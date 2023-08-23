def reverse_vowels(s):
    vowels = "AEIOUaeiou"
    s_list = list(s)
    vowels_in_s = [char for char in s if char in vowels]
    vowels_in_s.reverse()
    j = 0
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = vowels_in_s[j]
            j += 1
    return ''.join(s_list)



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