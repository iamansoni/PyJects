from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('E:/AMAN/Projects/Python/QR Code/qrcode.png')

result = decode(img)
print(result)