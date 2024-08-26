def idToShortURL(n):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""
    while n:
        shortURL.append(map[n % 62])
        n //= 62
    shortURL = reversed(shortURL)
    return shortURL

def shortURLtoID(shortURL):
    id = 0
    for i in range(len(shortURL)):
        if shortURL[i] in range("a", "z"):
            id = id * 62 + shortURL[i] - 'a'
        if shortURL[i] in range("A", "Z"):
            id = id * 62 + shortURL[i] - 'A' + 26
        if shortURL[i] in range("0", "9"):
            id = id * 62 + shortURL[i] - '0' + 52
    return id

url = "https://www.linkedin.com/in/maneesha-juneja-59a33695/"

id = shortURLtoID(url)

print("ID : ",  id)

shortURL = idToShortURL(id)

print("Short URL : ", shortURL)
