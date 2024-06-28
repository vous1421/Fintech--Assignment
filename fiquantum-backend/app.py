from flask import Flask, request, jsonify
from flask_cors import CORS 
from qiskit import Aer
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import COBYLA
from qiskit.utils import QuantumInstance
from qiskit.algorithms import VQE
from qiskit.opflow import PauliSumOp

# Create a Flask application instance
app = Flask(__name__)
CORS(app)

def optimize_portfolio(data):
    """
    Optimize the portfolio based on the provided data.

    Parameters:
    - data (dict): A dictionary containing Hamiltonian lists, weights, and optimizer parameters.

    Returns:
    - weighted_result (float): The computed weighted result.
    """
    # Extract Hamiltonians, weights, and optimizer parameters from input data
    hamiltonians = data.get('hamiltonians', [])
    weights = data.get('weights', [])
    optimizer_params = data.get('optimizer', {"name": "COBYLA", "maxiter": 100})
    
    # Convert Hamiltonian lists to PauliSumOp objects
    pauli_sum_ops = [PauliSumOp.from_list(ham) for ham in hamiltonians]

    # Define the number of qubits and the ansatz
    num_qubits = 4
    ansatz = TwoLocal(num_qubits, 'ry', 'cz', reps=3, entanglement='full')
    optimizer = COBYLA(maxiter=optimizer_params.get('maxiter', 100))
    quantum_instance = QuantumInstance(Aer.get_backend('aer_simulator_statevector'))
    vqe = VQE(ansatz, optimizer, quantum_instance=quantum_instance)

    # Compute the minimum eigenvalue for each Hamiltonian and store the results
    results = [vqe.compute_minimum_eigenvalue(ham).eigenvalue.real for ham in pauli_sum_ops]
    
    # Compute the weighted result by combining results with their corresponding weights
    weighted_result = sum(w * r for w, r in zip(weights, results))
    
    return weighted_result

@app.route('/optimize', methods=['POST'])
def optimize():
    """
    API endpoint to optimize the portfolio.
    
    Expects a JSON payload with Hamiltonians, weights, and optimizer parameters.
    Returns the computed weighted result as a JSON response.
    """
    data = request.json
    result = optimize_portfolio(data)
    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
