import hashlib

base = "ojvtpuvg"
result = ""
counter = 0
while True:
    hash = hashlib.md5((base + str(counter)).encode('utf-8')).hexdigest()
    if hash[:5] == "00000":
        result += hash[5]
        print(result)
        if len(result) == 8:
            break
    counter += 1
