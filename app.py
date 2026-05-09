from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import subprocess
import re

app = Flask(__name__)
CORS(app)

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

@app.route('/api/rules', methods=['GET'])
def get_rules():
    out, _ = run_cmd("iptables -L INPUT -n --line-numbers -v")
    out2, _ = run_cmd("iptables -L OUTPUT -n --line-numbers -v")
    out3, _ = run_cmd("iptables -L FORWARD -n --line-numbers -v")
    data = {"INPUT": out, "OUTPUT": out2, "FORWARD": out3}
    return jsonify(data)

@app.route('/api/rules', methods=['POST'])
def add_rule():
    data = request.json
    chain = data.get('chain', 'INPUT')
    src = data.get('src', '0.0.0.0/0')
    port = data.get('port', '')
    action = data.get('action', 'ACCEPT')
    proto = data.get('proto', 'tcp')
    cmd = "iptables -A " + chain + " -s " + src + " -p " + proto
    if port and port != '*':
        cmd = cmd + " --dport " + port
    cmd = cmd + " -j " + action
    out, err = run_cmd(cmd)
    if err:
        return jsonify({"status": "error", "message": err}), 400
    return jsonify({"status": "ok", "command": cmd})

@app.route('/api/rules/<chain>/<int:num>', methods=['DELETE'])
def delete_rule(chain, num):
    out, err = run_cmd("iptables -D " + chain + " " + str(num))
    if err:
        return jsonify({"status": "error", "message": err}), 400
    return jsonify({"status": "ok"})

@app.route('/api/enable', methods=['POST'])
def enable():
    run_cmd("iptables -P INPUT DROP")
    run_cmd("iptables -P FORWARD DROP")
    run_cmd("iptables -P OUTPUT ACCEPT")
    run_cmd("iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
    return jsonify({"status": "enabled"})

@app.route('/api/disable', methods=['POST'])
def disable():
    run_cmd("iptables -P INPUT ACCEPT")
    run_cmd("iptables -P FORWARD ACCEPT")
    run_cmd("iptables -P OUTPUT ACCEPT")
    run_cmd("iptables -F")
    return jsonify({"status": "disabled"})

@app.route('/api/flush', methods=['POST'])
def flush():
    run_cmd("iptables -F")
    return jsonify({"status": "flushed"})

@app.route('/api/status', methods=['GET'])
def status():
    out, _ = run_cmd("iptables -L INPUT --line-numbers -n")
    match = re.search(r'Chain INPUT \(policy (\w+)\)', out)
    policy = match.group(1) if match else 'UNKNOWN'
    lines = [l for l in out.split('\n') if l.strip() and not l.startswith('Chain') and not l.startswith('target')]
    return jsonify({"policy": policy, "rule_count": len(lines)})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
