import hashlib #libraria e marr ne baze te ushtrimeve ne klase
print("Goodbye, World!")
#fillimisht po e gjenerojme nje key stream me nje string seed
def generate_keystream(seed, message_length):

    if isinstance(seed, str):
        seed = seed.encode('utf-8') #duhet me bo utf-8 qe me konvertu seeds ne byte
    seed = int.from_bytes(hashlib.sha256(seed).digest(), byteorder='big')
    keystream = []
    for i in range(message_length):
        seed ^= seed<<13 
        seed ^= seed>>17 
        seed ^= seed<<5 
        num = seed & 0x7fffffff 
        keystream.append(num % 256)
    return keystream    