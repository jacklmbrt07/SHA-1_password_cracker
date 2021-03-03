import hashlib

def crack_sha1_hash(hash, use_salts=None):
    try:
        sha1_file = open('top-10000-passwords.txt', 'r')
    except:
        return "Error: File not found"
    # return the password if it is in the top 10000
    # else return "PASSWORD NOT IN DATABASE"
    
    for password in sha1_file.readlines():
        hash_obj = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
        if hash_obj == hash:
            return str(password)
        
    return "PASSWORD NOT IN DATABASE"
   