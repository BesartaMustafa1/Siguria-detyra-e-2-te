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

def otp_encrypt(message, seed):
    message_bytes = message.encode() #Mesazhi ne byte
    keystream = generate_keystream(seed, len(message_bytes)) #po e gjenerojm celesin
    encrypted_message = bytearray()  #E inicializojme mesazhin e enkriptuar
    for i in range(len(message_bytes)): #po enkriptojm
        encrypted_byte = message_bytes[i] ^ keystream[i]
        encrypted_message.append(encrypted_byte)
    return encrypted_message.hex() #mesazhi i enkriptuar

def otp_decrypt(encrypted_hex, seed):
    #Konverton mesazhin e koduar ne bajta duke perdorur formatin heksadecimal
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    
    #Gjenero nje celës me gjatesine e mesazhit te koduar ne bajta
    keystream = generate_keystream(seed, len(encrypted_bytes))
    
    #Krijon nje objekt bytearray per te ruajtur mesazhin e dekriptuar
    decrypted_message = bytearray()

   #unaza per te shkeputur cdo bajt te mesazhit
    for i in range(len(encrypted_bytes)):
        #Ben operacionin XOR midis bajtit te koduar dhe celesit
        decrypted_byte = encrypted_bytes[i] ^ keystream[i]
        #Shton bajtin e dekriptuar ne objektin bytearray
        decrypted_message.append(decrypted_byte)

    #Kthen mesazhin e dekriptuar në forme teksti
    return decrypted_message.decode()
 
if __name__ == "__main__": #Kontrollojm a po behet run scripta si main program
    message = input('Shkruani nje tekst: ') #Useri shtyp mesazhin qe deshiron te enkriptohet
    seed = input('Jepni seed-in si integer ose string: ') #Useri jep vleren "seed" e cila mund te jete integer ose string

    encrypted_message = otp_encrypt(message, seed) #Therret funksionin "otp_encrypt" dhe e enkripton mesazhin me seed-in qe jep useri
    print('Mesazhi i enkriptuar: ' + encrypted_message) #Shfaq mesazhin e enkriptuar

    #Provojm qe programi ta pyes userin se a deshiron te dekriptoj mesazhin nese "po" ta shfaq mesazhin e dekriptuar nese "jo" printon nje tekst whatever.