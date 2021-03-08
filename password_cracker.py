import hashlib

def crack_sha1_hash(hash, use_salts=None):
    try:
        sha1_file = open('top-10000-passwords.txt', 'r').readlines()
        known_salts = open('known-salts.txt', 'r').readlines()
    except:
        return "Error: File not found"
    
    if not use_salts == True:
        for password in sha1_file:
            hash_obj = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
            if hash_obj == hash:
                password = password.split('\n')
                return password[0]
    
    else:
        for password in sha1_file:
            password = password.strip() 
            for salt in known_salts:
                salt = salt.strip() 
                hashwords = [salt+password, password+salt]
                for hashword in hashwords:
                    hash_obj = hashlib.sha1(hashword.strip().encode('utf-8')).hexdigest()
                    if hash_obj == hash:
                        password = password.split('\n')
                        return password[0]
                   
    return "PASSWORD NOT IN DATABASE"
   