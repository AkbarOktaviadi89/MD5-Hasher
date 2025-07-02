import hashlib

def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()
