import socket
import time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',1234))
time.sleep(2)
while True:	
	message = raw_input("请输入你要发送给服务器的信息")
	sock.send(message)
	#print sock.recv(1024)
	#sock.close()
