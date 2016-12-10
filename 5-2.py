import hashlib

base = "ojvtpuvg"
result = "________"
print(result)
counter = 0
while True:
    hash = hashlib.md5((base + str(counter)).encode('utf-8')).hexdigest()
    if hash[:5] == "00000":
        try:
            position = int(hash[5])
            if position < 8 and result[position] == "_":
                lista = list(result)
                lista[position] = hash[6]
                result = "".join(lista)
                print(result)
        except:
            pass
        if result.count("_") == 0:
            break
    counter += 1
