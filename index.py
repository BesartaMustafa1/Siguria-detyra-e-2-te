import hashlib #libraria e marr ne baze te ushtrimeve ne klase
print("Goodbye, World!")
#fillimisht po e gjenerojme nje key stream me nje string seed
def generate_keystream(seed, message_length):

    if isinstance(seed, str):
        seed = seed.encode('utf-8') #duhet me bo utf-8 qe me konvertu seeds ne byte
    seed = int.from_bytes(hashlib.sha256(seed).digest(), byteorder='big')
    keystream = []
    #Per keystream-in e perdorim XOR-shifts
    for i in range(message_length):
        seed ^= seed<<13 #Kjo ben shift vleren "seed" majtas per 13 pozisione, pastaj ben kete vler XOR me vleren e vjeter "seed"
        seed ^= seed>>17 #Kjo ben shift vleren "seed" djathas per 17 pozisione dhe pastaj ben kete vler XOR me vleren e vjeter "seed"
        seed ^= seed<<5 #Kjo ben shift vleren "seed" majtas per 5 pozisione dhe pastaj ben kete vler XOR me vleren e vjeter "seed"
        num = seed & 0x7fffffff #Ketu vetem 31 bitet me te majt te vleres "seed" jane perdorur qe ne fund numri te jete pozitiv
        keystream.append(num % 256) #Ketu sigurohet qe vlera perfundimtare te jete ne mes 0 dhe 255(e moduluar me 255), kete eben duke e zbritur numrin e percaktuar me 256
    return keystream    
#Ne vazhdim funksioni one time pad encryption (otp_encrypt)

def etp_encrypt(message, seed):
    message_bytes = message.encode()
    keystream = generate_keystream(seed, len(message_bytes))
    encrypted_message = bytearray()