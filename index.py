import hashlib #libraria e marr ne baze te ushtrimeve ne klase
print("Goodbye, World!")
#fillimisht po e gjenerojme nje key stream me nje string seed
def generate_keystream(seed,message_length):
    if isinstance(seed,str):
        seed=seed.encode('utf-8')
        