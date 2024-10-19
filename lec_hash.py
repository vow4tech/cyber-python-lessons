import hashlib as hl
saved_pwd = '1234a'

def hash_pwd(ps):
    ps = ps.encode('utf-8')
    h=hl.sha256(ps)
    ms = h.hexdigest()
    return ms

def check_pwd(ps1, ps2):
    ps1_h = hash_pwd(ps1)
    ps2_h =  hash_pwd(ps2)
    return ps1_h == ps2_h

ent_pwd = input("ENter pswd ")
if check_pwd(saved_pwd, ent_pwd):
    print("Access Granted")
else:
    print('Access Denied')