from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver= ('127.0.0.1', 1025)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket= socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mail_command =('MAIL FROM: eee7225@nyu.edu>rn')
    clientSocket.send(mail_command.encode())
    recv2= clientSocket.recv(1024).decode()

    # Send RCPT TO command and handle server response.
    rcpt_command= ('RCPT TO: achievepm@yahoo.com>rn')
    clientSocket.send(rcpt_command.encode())
    recv3= clientSocket.recv(1024).decode()

    # Send DATA command and handle server response.
    data = "DATA rn"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message data.
    subject ="Subject : Testing my mailrnrn"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())

    # Message ends with a single period, send message end and handle server response.
    recv_msg = clientSocket.recv(1024)
    quitcommand = ('QUITrn')
    clientSocket.send(quitcommand.encode())
    recv5= clientSocket.recv(1024).decode()

    # Send QUIT command and handle server response.
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')