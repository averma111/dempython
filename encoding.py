import base64

key=base64.b64encode(b'this is password');

print("This is encoded key:",key)

decrypt=base64.decodestring(key);

print("This is original key:",decrypt);
