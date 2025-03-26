import unittest
from cryptography.fernet import Fernet
import jwt
from src.security import SecurityManager

class TestSecurityManager(unittest.TestCase):

    def setUp(self):
        self.encryption_key = Fernet.generate_key()
        self.jwt_secret = 'test_jwt_secret'
        self.security_manager = SecurityManager(self.encryption_key, self.jwt_secret)

    def test_encrypt_decrypt_data(self):
        data = "test_data"
        encrypted_data = self.security_manager.encrypt_data(data)
        self.assertIsNotNone(encrypted_data)
        decrypted_data = self.security_manager.decrypt_data(encrypted_data)
        self.assertEqual(decrypted_data, data)

    def test_generate_verify_jwt(self):
        payload = {"node_id": "123", "role": "participant"}
        token = self.security_manager.generate_jwt(payload)
        self.assertIsNotNone(token)
        verified_payload = self.security_manager.verify_jwt(token)
        self.assertEqual(verified_payload, payload)

    def test_authorize_node(self):
        payload = {"node_id": "123", "role": "participant"}
        token = self.security_manager.generate_jwt(payload)
        is_authorized = self.security_manager.authorize_node(token, "participant")
        self.assertTrue(is_authorized)

    def test_encrypt_data_error_handling(self):
        with self.assertLogs(level='ERROR'):
            encrypted_data = self.security_manager.encrypt_data(None)
            self.assertIsNone(encrypted_data)

    def test_decrypt_data_error_handling(self):
        with self.assertLogs(level='ERROR'):
            decrypted_data = self.security_manager.decrypt_data(b'invalid_data')
            self.assertIsNone(decrypted_data)

    def test_generate_jwt_error_handling(self):
        with self.assertLogs(level='ERROR'):
            token = self.security_manager.generate_jwt(None)
            self.assertIsNone(token)

    def test_verify_jwt_error_handling(self):
        with self.assertLogs(level='ERROR'):
            payload = self.security_manager.verify_jwt('invalid_token')
            self.assertIsNone(payload)

    def test_authorize_node_error_handling(self):
        with self.assertLogs(level='ERROR'):
            is_authorized = self.security_manager.authorize_node('invalid_token', 'participant')
            self.assertFalse(is_authorized)

if __name__ == '__main__':
    unittest.main()
