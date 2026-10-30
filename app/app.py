
from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests"
)

ERROR_COUNT = Counter(
    "app_errors_total",
    "Total number of HTTP errors"
)


@app.before_request
def count_request():
    REQUEST_COUNT.inc()


@app.after_request
def count_errors(response):
    if response.status_code >= 400:
        ERROR_COUNT.inc()
    return response


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from DevOps CI/CD Project!",
        "application": "Flask Demo",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


@app.route("/error")
def error():
    return jsonify({"error": "Sample error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
