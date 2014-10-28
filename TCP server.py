from socket import *
import select

serversock = socket(AF_INET,SOCK_STREAM)
serversock.bind(('',5001))
serversock.listen(5)

conn = serversock.accept()
addr = serversock.accept()

print 'started....' , addr
while 1:
	data = conn.recv(1024)
	print 'come'
	if not data:
		print 'break', data
		break
	conn.send(data)
	print 'out'

conn.close()
