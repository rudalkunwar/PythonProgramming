import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = "My name is Rudal kunwar xoxox"
qr.add_data(data)
qr.make(fit=True)
img1 = qr.make_image(fill='blue', back_color='red')  # Fix the method name here
img1.save('1.png')
