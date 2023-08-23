def read_file_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                cleaned_line = line.strip()
                print(f'- {cleaned_line}')
    except FileNotFoundError:
        print(f"Error: Thr file '{filename}' cannot be found.")




    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!