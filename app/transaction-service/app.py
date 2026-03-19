from flask import Flask, jsonify, request
import logging
import datetime

app = Flask(__name__)

# Configure logging (production style)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# In-memory database (mock)
transactions = []

@app.route("/")
def home():
    return jsonify({"message": "Transaction Service Running"}), 200

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/transactions", methods=["POST"])
def create_transaction():
    data = request.get_json()

    transaction = {
        "id": len(transactions) + 1,
        "amount": data.get("amount"),
        "type": data.get("type"),
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

    transactions.append(transaction)

    logging.info(f"Transaction created: {transaction}")

    return jsonify(transaction), 201

@app.route("/transactions", methods=["GET"])
def get_transactions():
    return jsonify(transactions), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
