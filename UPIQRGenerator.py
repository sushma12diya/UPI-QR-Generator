import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# UPI payment format
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes as image files
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()