import ipfshttpclient
import logging

class IPFSClient:

    def __init__(self, ipfs_address='/dns/localhost/tcp/5001/http'):
        self.client = ipfshttpclient.connect(ipfs_address)

    def upload_file(self, file_path):
        try:
            res = self.client.add(file_path)
            logging.info(f"File uploaded to IPFS: {res['Hash']}")
            return res['Hash']
        except Exception as e:
            logging.error(f"Error uploading file to IPFS: {e}")
            return None

    def download_file(self, file_hash, output_path):
        try:
            self.client.get(file_hash, target=output_path)
            logging.info(f"File downloaded from IPFS: {file_hash}")
        except Exception as e:
            logging.error(f"Error downloading file from IPFS: {e}")

    def store_model_update(self, model_update):
        try:
            res = self.client.add_bytes(model_update.encode('utf-8'))
            logging.info(f"Model update stored in IPFS: {res}")
            return res
        except Exception as e:
            logging.error(f"Error storing model update in IPFS: {e}")
            return None

    def retrieve_model_update(self, model_update_hash):
        try:
            model_update = self.client.cat(model_update_hash).decode('utf-8')
            logging.info(f"Model update retrieved from IPFS: {model_update_hash}")
            return model_update
        except Exception as e:
            logging.error(f"Error retrieving model update from IPFS: {e}")
            return None
