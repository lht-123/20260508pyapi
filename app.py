import logging
from flask import Flask, jsonify
import sys

# 配置日志格式，输出到标准输出（便于 docker logs 查看）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("Request received on /")
    return jsonify({"message": "Hello, World from Flask!202605080000000000000000000000000000000000000000"})

@app.route('/health')
def health():
    logger.info("Health check")
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    logger.info("Starting Flask application on port 8080...")
    app.run(host='0.0.0.0', port=8080)