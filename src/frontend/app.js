document.addEventListener('DOMContentLoaded', function() {
    const statusText = document.getElementById('status-text');
    const joinForm = document.getElementById('join-form');

    joinForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const nodeId = document.getElementById('node-id').value;
        joinFederatedLearning(nodeId);
    });

    function joinFederatedLearning(nodeId) {
        // Implement the logic to join federated learning
        // For now, we'll just update the status text
        statusText.textContent = `Node ${nodeId} has joined the federated learning process.`;
    }

    function updateStatus(status) {
        statusText.textContent = status;
    }

    function handleError(error) {
        console.error(error);
        statusText.textContent = 'An error occurred. Please try again.';
    }

    // Example function to communicate with the backend using gRPC
    function sendModelUpdate(modelUpdate) {
        // Implement the gRPC communication logic here
        // For now, we'll just log the model update
        console.log(`Sending model update: ${modelUpdate}`);
    }

    // Example function to receive model updates from the backend using gRPC
    function getModelUpdates() {
        // Implement the gRPC communication logic here
        // For now, we'll just log a message
        console.log('Receiving model updates...');
    }

    // Example usage
    sendModelUpdate('example_model_update');
    getModelUpdates();
});
