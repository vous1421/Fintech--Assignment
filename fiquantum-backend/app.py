from flask import Flask, request, jsonify
from flask_cors import CORS 
from qiskit import Aer
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import COBYLA
from qiskit.utils import QuantumInstance
from qiskit.algorithms import VQE
from qiskit.opflow import PauliSumOp

app = Flask(__name__)
CORS(app)

def optimize_portfolio(data):
    hamiltonians = data.get('hamiltonians', [])
    weights = data.get('weights', [])
    optimizer_params = data.get('optimizer', {"name": "COBYLA", "maxiter": 100})
    
    pauli_sum_ops = [PauliSumOp.from_list(ham) for ham in hamiltonians]
    
    num_qubits = 4
    ansatz = TwoLocal(num_qubits, 'ry', 'cz', reps=3, entanglement='full')
    optimizer = COBYLA(maxiter=optimizer_params.get('maxiter', 100))
    quantum_instance = QuantumInstance(Aer.get_backend('aer_simulator_statevector'))
    vqe = VQE(ansatz, optimizer, quantum_instance=quantum_instance)
    
    results = [vqe.compute_minimum_eigenvalue(ham).eigenvalue.real for ham in pauli_sum_ops]
    weighted_result = sum(w * r for w, r in zip(weights, results))
    
    return weighted_result

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    result = optimize_portfolio(data)
    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
