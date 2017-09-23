words = ["wednesdaythursday","wednesdaysaturday","thursdaywednesday","saturdaywednesday"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
c = "eplxiuuynlozlrshw"

key = ""

print("len of c " + str(len(c)))


for word in words:
    for i,char in enumerate(word):
        shift = (alphabet.index(c[i]) - alphabet.index(char)) % 26
        key += alphabet[shift]
    print("Key for " + word + " is " + key)
    key = ""
