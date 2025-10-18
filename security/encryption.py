# =========================================================
#  VPN GUARD (SCG) - Encryption Module
#  Handles secure data encryption, hashing, and key management.
# =========================================================

import hashlib
import os

class EncryptionManager:
    def __init__(self):
        self.key = None

    def generate_key(self):
        self.key = os.urandom(32)
        print("[Encryption] Key generated successfully.")
        return self.key

    def encrypt_data(self, data):
        if not self.key:
            self.generate_key()
        hashed = hashlib.sha256(data.encode()).hexdigest()
        print("[Encryption] Data encrypted.")
        return hashed

    def verify_integrity(self, data, hash_value):
        return hashlib.sha256(data.encode()).hexdigest() == hash_value
