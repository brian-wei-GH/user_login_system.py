import hashlib

def security_md5(user_psw):
    salt = "dofjoefj939oejfnodno83998oppjono399"  # define by yourself (to increase security level)
    obj = hashlib.md5(salt.encode('utf-8'))
    obj.update(user_psw.encode('utf-8'))
    res = obj.hexdigest()
    return res
