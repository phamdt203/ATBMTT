import hashlib

def hash(data):
    hash_object = hashlib.md5()
    hash_object.update(data.encode())
    hash_value = hash_object.hexdigest()
    return str(hash_value).split()
