from flask import Flask, request

app = Flask(__name__)

ip_req_count = 0

@app.route('/')
def count_ip_requests():
    global ip_req_count
    ip_addr = request.remote_addr
    ip_req_count = ip_req_count + 1

    result = "IP address: " + str(ip_addr) + " | Request count: " + str(ip_req_count)

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
