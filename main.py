import hashlib

def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def compare_md5(text, hash_to_compare):
    return generate_md5(text) == hash_to_compare.lower()


