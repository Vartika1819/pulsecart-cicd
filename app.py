from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>PulseCart | Live Delivery</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #101827;
          color: white;
          text-align: center;
          padding: 70px 20px;
        }
        .card {
          max-width: 650px;
          margin: auto;
          padding: 35px;
          background: #1e293b;
          border-radius: 18px;
        }
        h1 { color: #38bdf8; font-size: 42px; }
        .status { color: #4ade80; font-size: 22px; }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>PulseCart</h1>
        <h2>Smart Delivery Tracking</h2>
        <p class="status">● All systems operational</p>
        <p>Your orders, moving smarter.</p>
        <p>Release: v1.0 | Powered by Kubernetes</p>
      </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
