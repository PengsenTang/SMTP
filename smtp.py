from socket import *
import time

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.163.com',25)

# Fill in start   #Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Login ...
clientSocket.send('auth login\r\n')
recv1 = clientSocket.recv(1024)
print(recv1)
clientSocket.send('cGVuZ3NlbjgwMDA=\r\n')
recv1 = clientSocket.recv(1024)
clientSocket.send('MTIzNDU2Nzg=\r\n')
recv1 = clientSocket.recv(1024)
print(recv1)


# Send MAIL FROM command and print server response.
# Fill in start
clientSocket.send("MAIL FROM:<" + "pengsen8000@163.com" + ">\r\n")
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
clientSocket.send("RCPT TO:<" + "491469748@qq.com" + ">\r\n")
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send('data\r\n')
recv1 = clientSocket.recv(1024)
print(recv1)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send("from:pengsen8000@163.com\r\n")
clientSocket.send("to:491469748@qq.com\r\n")
clientSocket.send("subject:A survey on SMTP!\r\n")
clientSocket.send("\r\n")
present = time.localtime()
clientSocket.send('This is a demo from python at ' + time.strftime('%m/%d/%H:%M:%S', present) + '\r\n')


# Fill in end
# Message ends with a single period.
# Fill in start

clientSocket.send('.')

# Fill in end

# Send QUIT command and get server response.
# Fill in start

clientSocket.send(endmsg)
recv1 = clientSocket.recv(1024)
print(recv1)
# Fill in end
