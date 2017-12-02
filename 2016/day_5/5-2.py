import hashlib
import random

base = "ojvtpuvg"
result = "________"
letters = "abcdefghijklmnopqrstuvwxyz#$?/*()+="
counter = 0
print(result, end="")
while True:
    hash = hashlib.md5((base + str(counter)).encode('utf-8')).hexdigest()
    if hash[:5] == "00000":
        try:
            position = int(hash[5])
            if position < 8 and result[position] == "_":
                lista = list(result)
                lista[position] = hash[6]
                result = "".join(lista)
        except:
            pass
        if result.count("_") == 0:
            break

    # provides nice animation
    if counter % 10000 == 0:
        toprint = ""
        for char in result:
            if char == "_": toprint += random.choice(letters)
            else: toprint += char
        print("\r" + toprint, end="")
    counter += 1
