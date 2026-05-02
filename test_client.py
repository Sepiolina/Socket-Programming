from pyexpat.errors import messages
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',2345))
#wrong
massage = '5609610760:070'
s.send(massage.encode())
data = s.recv(1024)
print(data.decode())
#wrong
massage = '5609610760:070'
s.send(massage.encode())
data = s.recv(1024)
print(data.decode())
#right
massage = '5609610760:0706'
s.send(massage.encode())
data = s.recv(1024) #get token
print(data.decode())
#wrong
token = "NTYwOOOTYeec2MC4wezA2Lmtle==:check secret number:40"
s.send(token.encode())
data2 = s.recv(1024)
print(data2.decode())
#wrong
token0 = "wrongtoken:check secret number:3"
s.send(token0.encode())
data2 = s.recv(1024)
print(data2.decode())
#================= from now on right request send =================
token1 = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:request secret number:5:221"
s.send(token1.encode())
data2 = s.recv(1024) #receive auth response
print(data2.decode())
data2 = s.recv(1024) #receive message response
print(data2.decode())

token2 = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:check secret number:3"
s.send(token2.encode())
data2 = s.recv(1024) #receive auth response
print(data2.decode())
data4 = s.recv(1024) #receive message response
print(data4.decode())

token3 = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:check secret number:33"
s.send(token3.encode())
data2 = s.recv(1024) #receive auth response
print(data2.decode())
data3 = s.recv(1024) #receive message response
print(data3.decode())

token = "NTYwOTYxMDc2MC4wNzA2LmtleQ==:quit"
s.send(token.encode())
data2 = s.recv(1024) #receive auth response
print(data2.decode())
data5 = s.recv(1024) #receive message response
print(data5.decode())

