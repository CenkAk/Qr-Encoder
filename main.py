import qrcode

data = input("Input your data: ")

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'purple', back_color = 'white')

img.save('C:/Users/cenka/Documents/WORKSPACE/py/qrencoder/qr/qr1.png')