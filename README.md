# Fintech--Assignment
# FiQuantum

FiQuantum is a quantum computing-based financial analysis platform designed to optimize portfolios and model financial risks using advanced quantum algorithms.

## Features

- **Quantum Portfolio Optimization**: Leverages quantum algorithms to find optimized asset allocations.
- **Quantum Risk Modeling**: Utilizes quantum computing power to build sophisticated risk models.

## Technology Stack

- **Frontend**: React
- **Backend**: Flask
- **Quantum Computing**: Qiskit

## Setup

### Frontend

1. Navigate to the `fiquantum-frontend` directory.
    ```bash
    cd fiquantum-frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the frontend server:
    ```bash
    npm start
    ```

### Backend

1. Navigate to the `fiquantum-backend` directory.
    ```bash
    cd fiquantum-backend
    ```
2. Create and activate virtual environment:
    ```bash
    conda create -n fiquantum-env python=3.9
    conda activate fiquantum-env
    ```
3. Install dependencies:
    ```bash
    pip install flask
    pip install qiskit==0.39.0
    ```
4. Start the backend server:
    ```bash
    python app.py
    ```

## Usage

1. Open the frontend application in your browser.
2. Input data for portfolio optimization. Example input:
    ```json
       [
      ["IIIZ", -1],
      ["IIZI", 1],
      ["IZII", 1],
      ["ZIII", -1],
      ["XXII", 0.5],
      ["YYII", 0.5],
      ["ZZII", 0.5]
    ]
    ```
3. Submit to see the optimized result.
