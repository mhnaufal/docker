from flask import Flask, request

app = Flask(__name__)

ips_list = {}

@app.route('/')
def count_ip_requests():
    ip_addr = request.remote_addr

    # find existing IP in hashmap
    if str(ip_addr) in ips_list:
        ips_list[str(ip_addr)] = ips_list[str(ip_addr)] + 1
    else:
        ips_list[str(ip_addr)] = 1

    result = "IP address: " + str(ip_addr) + " | Request count: " + str(ips_list[str(ip_addr)])

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
