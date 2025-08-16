from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Firebase Admin SDK (service account key)
cred = credentials.Certificate("serviceAccountKey.json")  # Download from Firebase console
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()  # Get JSON from frontend
        db.collection("users").add(data)  # Save to Firestore
        return jsonify({"message": "Data stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
