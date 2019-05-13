import socket

def saveFile(data,fileName):
    print(fileName)
    file = open(fileName, "wb")
    i = 0 
    while i<len(data):
        file.write(data[i])
        i += 1 
    file.close()
    return 
    
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ip = socket.gethostbyname(socket.gethostname)
ip = "127.0.0.1"
port = 1222 
address = (ip , port)
server.bind(address)
server.listen(1)
print (ip,':',port)

while True:
    conn,addr = server.accept()
    try: 
        print("connected from",addr[0],':',addr[1])
        #file = open("rec.rec", "wb")
        datafile = []
        mode = "0"
        fileName =""
        counter = 0 ;
        while True:
            data = conn.recv(4096)
            if data:
                print ("recieve:",data)
                if data == "hello server!":
                    conn.send("hello client")
                elif data == "disconnect":
                    conn.send("bye")
                    conn.close()
                    break
                elif counter == 0:
                    mode = data
                    counter+=1
                elif counter == 1:
                    fileName = data
                    counter+=1
                    if counter == 2 and mode == "2":
                        with open(fileName, "rb") as file:
                            # send file
                            print("Sending file ...")
                            # read the whole file at once
                            dataUp = file.read()
                            # Convert the file into smaller segments and send them
                            conn.send(dataUp)
                            print("sending to client completed!")
                            #file.close()
                        counter+=1
                        break
                else:
                    # write bytes on file
                    datafile.append(data)
                    #file.write(data)
            else:
                print("no data!")
                saveFile(datafile,fileName)
                break
    finally:
        
        conn.close()
