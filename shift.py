words = ["rstu", "svux"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
for word in words:
    for x in range(26):
        shifted = ""
        for char in word:
            s_index = (alphabet.index(char) + x) % 26
            shifted += alphabet[s_index]
        print(word + " shifted by " + str(x) + ": " + str(shifted))
        shifted = ""
    print("")            



