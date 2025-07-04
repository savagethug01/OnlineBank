from .decorators import *
from .forms import *
from .models import *

# utils.py
def validate_bic(input_bic, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_bic == user_profile.bic_code

def validate_imf(input_imf, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_imf == user_profile.imf_code

def validate_tax(input_tax, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_tax == user_profile.tax_code

def validate_tac(input_tac, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_tac == user_profile.tac_code

def validate_vat(input_vat, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_vat == user_profile.vat_code

def validate_linking_code(input_linking_code, user_profile):
    # Compare the input OTP with the OTP stored in the user profile
    return input_linking_code == user_profile.linking_code
