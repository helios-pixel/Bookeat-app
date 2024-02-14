import rsa
(a_pub,a_priv) = rsa.newkeys(2024)
f=open('/home/kali/abc.txt', 'rb') # path of file
data=f.read()
data
(b_pub,b_priv)=rsa.newkeys(4024)
ciphertext1=rsa.encrypt(data,a_pub)
ciphertext1
ciphertext1=rsa.encrypt(ciphertext1,b_pub)
ciphertext1
f.close()
f=open('/home/kali/abc.txt','wb') # path of file
f.write(ciphertext1)
f.close()
dec_text=rsa.decrypt(ciphertext1,b_priv)
dec_text
dec_text=rsa.decrypt(dec_text,a_priv)
dec_text