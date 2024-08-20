# OTP-VERIFICATION

```markdown
# OTP Verification System

This repository contains two Python scripts for OTP verification:
1. **Email-based OTP Verification** using Gmail.
2. **SMS-based OTP Verification** using Twilio.
```

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Himanshu-Vishwakarma-GH/OTP-VERIFICATION.git
   cd OTP-VERIFICATION
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Email-based OTP
1. Update Gmail credentials in `Otp_(E-mail).py`.
2. Run the script:
   ```bash
   python Otp_(E-mail).py
   ```

### SMS-based OTP
1. Update Twilio credentials in `Otp_(Phone).py`.
2. Run the script:
   ```bash
   python Otp_(Phone).py
   ```

## Configuration
- **Email-based**: Update `sender_email`, `sender_password`, and `receiver_email`.
- **SMS-based**: Update `account_sid`, `auth_token`, `from_phone`, and `to_phone`.

## License
Licensed under the MIT License.

