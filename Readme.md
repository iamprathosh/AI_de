# Decentralized Federated Learning Platform

## Project Description

This project aims to develop a decentralized federated learning platform that enables collaborative training of large language models (LLMs) without sharing raw data. The platform leverages gRPC for efficient, low-latency inter-node communication and IPFS for decentralized storage of model updates and metadata. A serverless architecture is implemented to manage training tasks, ensuring scalability and cost-effectiveness. Data privacy is prioritized by keeping raw data on local nodes and sharing only model updates. The system is designed to be fault-tolerant, capable of handling node failures without disrupting the training process. Robust security measures, including encryption for data in transit and at rest, along with authentication and authorization mechanisms, are incorporated to ensure only authorized nodes participate in the federated learning process. The platform is modular, allowing for future enhancements and integration with other decentralized AI protocols.

## Architecture

The architecture of the decentralized federated learning platform consists of the following components:

- **gRPC**: Used for efficient, low-latency inter-node communication.
- **IPFS**: Utilized for decentralized storage of model updates and metadata.
- **Serverless**: Manages training tasks, ensuring scalability and cost-effectiveness.

## Setup Instructions

### Dependencies

- Python 3.8+
- gRPC
- IPFS
- Serverless framework

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/iamprathosh/AI_de.git
   cd AI_de
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

### Starting the Platform

1. Start the gRPC server:
   ```bash
   python src/server.py
   ```

2. Start the IPFS daemon:
   ```bash
   ipfs daemon
   ```

3. Deploy the serverless functions:
   ```bash
   serverless deploy
   ```

### Participating in Federated Learning

1. Start the gRPC client:
   ```bash
   python src/client.py
   ```

2. Follow the prompts to send and receive model updates.

## Contributing

We welcome contributions to the project! Please follow these guidelines when contributing:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write tests for your changes.
4. Ensure all tests pass.
5. Submit a pull request with a clear description of your changes.

## User Manual

### First-Time Setup

1. Ensure you have Python 3.8+ installed on your system.
2. Install the required dependencies by following the setup instructions above.
3. Start the gRPC server, IPFS daemon, and deploy the serverless functions as described in the usage instructions.

### Running the Platform

1. Start the gRPC server:
   ```bash
   python src/server.py
   ```

2. Start the IPFS daemon:
   ```bash
   ipfs daemon
   ```

3. Deploy the serverless functions:
   ```bash
   serverless deploy
   ```

4. Start the gRPC client:
   ```bash
   python src/client.py
   ```

5. Follow the prompts to send and receive model updates.

### Troubleshooting

- If you encounter any issues, please check the logs for error messages.
- Ensure that all dependencies are installed correctly.
- Verify that the gRPC server, IPFS daemon, and serverless functions are running properly.
- If the issue persists, please open an issue on the GitHub repository with detailed information about the problem.
