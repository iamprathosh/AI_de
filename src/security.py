import logging
from cryptography.fernet import Fernet
import jwt

class SecurityManager:

    def __init__(self, encryption_key, jwt_secret):
        self.encryption_key = encryption_key
        self.cipher = Fernet(encryption_key)
        self.jwt_secret = jwt_secret

    def encrypt_data(self, data):
        try:
            encrypted_data = self.cipher.encrypt(data.encode('utf-8'))
            logging.info("Data encrypted successfully")
            return encrypted_data
        except Exception as e:
            logging.error(f"Error encrypting data: {e}")
            return None

    def decrypt_data(self, encrypted_data):
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data).decode('utf-8')
            logging.info("Data decrypted successfully")
            return decrypted_data
        except Exception as e:
            logging.error(f"Error decrypting data: {e}")
            return None

    def generate_jwt(self, payload):
        try:
            token = jwt.encode(payload, self.jwt_secret, algorithm='HS256')
            logging.info("JWT generated successfully")
            return token
        except Exception as e:
            logging.error(f"Error generating JWT: {e}")
            return None

    def verify_jwt(self, token):
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
            logging.info("JWT verified successfully")
            return payload
        except Exception as e:
            logging.error(f"Error verifying JWT: {e}")
            return None

    def authorize_node(self, token, required_role):
        try:
            payload = self.verify_jwt(token)
            if payload and payload.get('role') == required_role:
                logging.info("Node authorized successfully")
                return True
            else:
                logging.warning("Node authorization failed")
                return False
        except Exception as e:
            logging.error(f"Error authorizing node: {e}")
            return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    encryption_key = Fernet.generate_key()
    jwt_secret = 'your_jwt_secret'
    security_manager = SecurityManager(encryption_key, jwt_secret)
    # Example usage
    encrypted_data = security_manager.encrypt_data("example_data")
    decrypted_data = security_manager.decrypt_data(encrypted_data)
    token = security_manager.generate_jwt({"node_id": "123", "role": "participant"})
    is_authorized = security_manager.authorize_node(token, "participant")
