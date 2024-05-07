import bcrypt
 

password = str(input("input password: ")) 
 

password = password.encode('utf-8')
 
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
print(hashed)
 
check = str(input("check password: ")) 
 
check = check.encode('utf-8') 
 
if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")