import string
import secrets
from .models import Coupon

def generate_coupn_code(length=10):
    characters = string.ascii_uppercase + string.digits

    while True:
        code= ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.object.filter(code = code).exists():
            return code