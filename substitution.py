def get_order(key):
    return sorted(range(len(key)),key=lambda k:key[k])
    
def encrypt(text,key):
    col=len(key)
    row=(len(text)+col-1)//col
    
    text+='x'*(row*col-len(text))
    
    mat=[]
    for i in range(0,len(text),col):
        mat.append(text[i:i+col])
    
    cipher=""
    for c in get_order(key):
        for r in range(row):
            cipher+=mat[r][c]
            
    return cipher
    
def decrypt(text,key):
    col=len(key)
    row=len(text)//col
    
    mat=[[""for _ in range(col)]for _ in range(row)]
    
    k=0
    for c in get_order(key):
        for r in range(row):
            mat[r][c]=text[k]
            k+=1
            
    
    result=""
    for r in mat:
        result+=''.join(r)
    return result.rstrip('x') 
    
text=input("Enter message:")
key=input("Enter key:")

clean=text.replace(" ","").lower()

encrypted=encrypt(clean,key)
print("Encrypted:",encrypted)

decrypted=decrypt(encrypted,key)
print("Decrypted:",decrypted)
        
    