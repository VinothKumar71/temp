import socket

f=open("index.html","w")
server_name="example.com"
server_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((server_name,server_port))

req=("GET / HTTP/1.1\r\n"
"HOST: example.com\r\n"
"CONNECTION: close\r\n"
"\r\n")

client.send(req.encode())

response=b""

while True:
    data=client.recv(4096)
    if not data:
        break
    response+=data
client.close()
f.write(response.decode())
print(response.decode())