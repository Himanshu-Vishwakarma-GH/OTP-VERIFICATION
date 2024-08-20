import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random

# Twilio credentials (twilio.com)
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Function to send OTP
def send_otp():
    global otp
    otp = random.randint(100000, 999999)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_='+12566085585',  # Your Twilio number
        to=mobile_entry.get()
    )
    messagebox.showinfo("OTP Sent", "OTP has been sent to your mobile number.")

# Function to verify OTP
def verify_otp():
    if int(otp_entry.get()) == otp:
        messagebox.showinfo("Success", "OTP verified successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

# GUI setup
root = tk.Tk()
root.title("OTP Verification System")

tk.Label(root, text="Enter Mobile Number:").pack(pady=5)
mobile_entry = tk.Entry(root)
mobile_entry.pack(pady=5)

tk.Button(root, text="Send OTP", command=send_otp).pack(pady=5)

tk.Label(root, text="Enter OTP:").pack(pady=5)
otp_entry = tk.Entry(root)
otp_entry.pack(pady=5)

tk.Button(root, text="Verify OTP", command=verify_otp).pack(pady=5)

root.mainloop()
