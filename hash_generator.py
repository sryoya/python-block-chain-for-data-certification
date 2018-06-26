import hashlib

hash = hashlib.sha256()
print(hash.block_size)
#with open('all.pdf', 'rb') as f:
        # chunk = f.read()
        # hash.update(chunk)
        # while True:
        #hash_value = hashlib.sha256(f.read()).hexdigest()
        #hash.update(f.read())
        #for chunk in iter(lambda: f.read(2048 * hash.block_size), b''):
            # if len(chunk) == 0:
            #     break
            #hash.update(chunk)
#hash_value = hashlib.sha256(("oh yeah").encode('UTF-8')).digest()
#hash_value = hash.hexdigest
file = open('sample_doc.pdf', 'rb')
hash_value = hashlib.sha256(file.read()).hexdigest()
print(hash_value)
