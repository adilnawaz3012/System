def idToShortURL(n):
    # Map to store 62 possible characters
    _map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = []
    # Convert given integer id to a base 62 number
    while n:
        shortURL.append(_map[n%62])
        n = n // 62

    # Reverse shortURL to complete base conversion
    shortURL = shortURL[::-1]
    return "".join(shortURL)

def shortURLtoID(shortURL):
    id = 0
    for i in range(0, len(shortURL)):
        if 'a' <= shortURL[i] <= 'z':
            id = id * 62 + ord(shortURL[i]) - ord('a')
        elif 'A' <= shortURL[i] <= 'Z':
            id = id * 62 + ord(shortURL[i]) - ord('A') + 26
        else:
            id = id * 62 - ord('0') + 52
    return id


url = "https://www.linkedin.com/in/maneesha-juneja-59a33695/"

id = shortURLtoID(url)

print("ID : ",  id)

shortURL = idToShortURL(id)

print("Short URL : ", shortURL)


"""
Note, first URL needs to be entered , then only we can fetch it using the ID generated.
"""