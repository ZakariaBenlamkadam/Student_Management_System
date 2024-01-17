import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

students = []
firstnames=[]

#broadcast:send one message to all the connected students
def broadcast(message):
    for student in students:
        student.send(message)

#handle: handling the connection
def handle(student):
    while True:
        try:
            message = student.recv(1024)  #.decode('utf-8')
            print(f"{firstnames[students.index(student)]} says {message}")
            broadcast(message)
        except:
            index = students.index(student)
            students.remove(student)
            student.close()
            firstname = firstnames[index]
            #broadcast(f'{firstname} left the chat'.encode('utf-8'))
            firstnames.remove(firstname)
            #firstnames.remove(firstname)
            break




#receive:listen listen accept new connections
def receive ():
    while True:
        student,address = server.accept()
        print(f"connected with {str(address)}!")

        student.send('FIRSTNAME'.encode('utf-8'))
        firstname = student.recv(1024) #bytes
        firstnames.append(firstname)
        students.append(student)

        print(f"Firstname of the student is {firstname}")
        broadcast(f"{firstname} connected to the server !\n".encode('utf-8'))
        student.send("connected to the server ".encode('utf-8'))

        thread= threading.Thread(target=handle, args=(student,))

        thread.start()

print("server running ")
receive()