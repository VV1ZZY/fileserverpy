import socket
import time



def SendRec(mode,namefile):
    client = socket.socket()
    client.connect(('127.0.0.1',1222))
    print("Connect to server!")
    client.send(mode)
    print("sent mode to server!")
    time.sleep(3)
    client.send(namefile)
    print("sent name of file to server!")
    time.sleep(3)
    if mode == "1":
        with open(namefile, "rb") as file:
            # send file
            print("Sending file ...")
            # read the whole file at once
            dataUp = file.read()
            # Convert the file into smaller segments and send them
            client.sendall(dataUp)
            print("upload completed!")
        #file.close()
    elif mode == "2":
        file = open(namefile, "wb")
        while True:
            data = client.recv(4096)
            print(data)
            if not data:
                file.close()
                break
            file.write(data) 
        client.close()
    return 


which = input('1-Upload 2-Download :\n')
fileName = input('Enter Name of File :(ex:"test.pdf)"\n')

SendRec(str(which),str(fileName))
