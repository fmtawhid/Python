# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC5012f84da6dc5bacb8633cf7533faa86"
auth_token = os.environ["bc1b3e36755b565a034d1903770b344d"]
verify_sid = "VAeafdcd08e70660133e85f62fced7c1b3"
verified_number = "+8801603747235"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)