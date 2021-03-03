import hashlib

def crack_sha1_hash(hash, use_salts=None):
    try:
        sha1_file = open('top-10000-passwords.txt', 'r').readlines()
        known_salts = open('known-salts.txt', 'r').readlines()
    except:
        return "Error: File not found"
    
    if not use_salts == True:
        for password in sha1_file.readlines():
            hash_obj = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
            if hash_obj == hash:
                return str(password)
    
    else:
        for password in sha1_file:
            password = password.strip().encode('utf-8')
            for salt in known_salts:
                salt = salt.strip().encode('utf-8')
                hash_obj = hashlib.pbkdf2_hmac('sha1', password=password, salt=salt, iterations=1000).hex()
                print(hash_obj)
                if hash_obj == hash:
                    return str(password) 
                   
    return "PASSWORD NOT IN DATABASE"
   