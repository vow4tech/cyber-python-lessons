import hashlib as hl

#data = "Hello World"
#print(hl.algorithms_available)

#md5_hashing = hl.md5()

#print(md5_hashing)


#sha256Hashing = hl.sha256(b'12345')

#print(sha256Hashing)

#msg_d = sha256Hashing.hexdigest()
#print(msg_d)

#saved password
#convert it to hashcode
#input password
#compare it with hashcode
#if similar, print granted successfull
#if not print denied 


passwordForNow = '12345678'
passwordForNowHashed = hl.sha256(b'12345678')
savedHash = passwordForNowHashed.hexdigest()
print("Saved is: ", savedHash)

enterPassword  = input("Enter Password: ")
enterPasswordHashed = hl.sha256(enterPassword)
enteredPasswordHashed = enterPasswordHashed.hexdigest()

print("Entered is: ", enteredPasswordHashed)

if(savedHash == enteredPasswordHashed):
    print("Granted Successfully")
else:
    print("Denied, Sorry")
