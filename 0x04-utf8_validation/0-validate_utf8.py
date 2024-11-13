#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Arguments:
    data -- A list of integers representing bytes of data.

    Returns:
    True if the data is a valid UTF-8 encoding, else False.
    """
    i = 0
    n = len(data)

    while i < n:
        byte = data[i]

        # Check for 1-byte character (0xxxxxxx)
        if byte <= 0x7F:
            i += 1
            continue

        # Check for 2-byte character (110xxxxx 10xxxxxx)
        elif byte >= 0xC0 and byte <= 0xDF:
            if i + 1 >= n or not (0x80 <= data[i + 1] <= 0xBF):
                return False
            i += 2

        # Check for 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
        elif byte >= 0xE0 and byte <= 0xEF:
            if i + 2 >= n or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF):
                return False
            i += 3

        # Check for 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        elif byte >= 0xF0 and byte <= 0xF7:
            if i + 3 >= n or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF) or not (0x80 <= data[i + 3] <= 0xBF):
                return False
            i += 4

        # If the byte doesn't match any of the above ranges, return False
        else:
            return False

    return True
