import hmac
import hashlib

def secure_hash(key, secret_salt):
    return hmac.new(secret_salt.encode(), key.encode(), hashlib.sha256).hexdigest()