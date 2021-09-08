from socket import *


def smtp_client(port=1025, mailserver="127.0.0.1"):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver = "127.0.0.1"
   port=1025

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, port))

   recv = clientSocket.recv(1024).decode()
   #print(recv)
   #if recv[:3] != '220':
       #print('220 reply not received from server.')
   # Send HELO command and print server response.
   heloCommand='HELO Alice\r\n'
   #print(heloCommand)
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   #if recv1[:3] != '250':
       #print('Helo 250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mailFromCMD = 'MAIL FROM: <robinsonacosta1@gmail.com>\r\n'
   #print(mailFromCMD)
   clientSocket.send(mailFromCMD.encode())
   recv2 = clientSocket.recv(1024).decode()
   #print("After MAIL FROM command:" + recv2)
   #if recv2[:3] != '250':
        #print('Mail from 250 reply not received from server.')

   # Send RCPT TO command and print server response.
   rcptToCMD = "RCPT TO: <ra3440@nyu.edu>\r\n"
   #print(rcptToCMD)
   clientSocket.send(rcptToCMD.encode())
   recv3 = clientSocket.recv(1024).decode()
   #print("After RCPT TO commands:"+recv3)
   #if recv3[:3] != '250':
       #print('Rcpt 250 reply not received from server.')

   # Send DATA command and print server response.
   dataCMD = 'DATA'
   #print(dataCMD)
   clientSocket.send(dataCMD.encode())
   recv4 = clientSocket.recv(1024).decode()
   #print("After DATA command: " + recv4)
   #if recv4[:3] != '250':
        #print('Data 250 reply not received from server.')
   
   # Send message data.
   clientSocket.send(msg.encode())
   # Message ends with a single period.
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024).decode()
   #print("After SEND: " + recv5)
 
   # Send QUIT command and get server response.
   quitCMD = 'QUIT\r\n'
   #print(quitCMD)
   clientSocket.send(quitCMD.encode())
   recv6 = clientSocket.recv(1024).decode()
   #print("After QUIT command: " + recv6)
   #if recv6[:3] != '250':
        #print('Quit 250 reply not received from server.')
  

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
