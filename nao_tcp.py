import socket

nao_ip = ''
nao_port = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((nao_ip, nao_port))

print("Connected to NAO at", nao_ip)

sock.close()
