import random

def encrypt(strings):
    n = random.randint(1, 10)

    encrypted_strings = []
    
   
    for string in strings:
        encrypted_string = []
        
       
        for char in string:
         
            unicode_value = ord(char)
            
           
            encrypted_unicode_value = unicode_value + n
            
           
            if encrypted_unicode_value > 126:
               
                encrypted_unicode_value = 33 + (encrypted_unicode_value - 33) % (126 - 33 + 1)
            
           
            encrypted_char = chr(encrypted_unicode_value)
            
           
            encrypted_string.append(encrypted_char)
        
       
        encrypted_strings.append(''.join(encrypted_string))
    
   
    return encrypted_strings, n


strings = ["senha", "mensagem", "segredo"]
encrypted_strings, key = encrypt(strings)
print("Chave de criptografia:", key)
print("Strings criptografadas:", encrypted_strings)