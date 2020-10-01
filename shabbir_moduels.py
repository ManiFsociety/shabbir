# if you can not understand source code read README.md 
import socket
from time import asctime as time
from time import sleep
from sys import exit
from re import findall as find
class color : 
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
    END = "\033[0m"

def menu():
        return f'''{color.red}
10100101000101010100101    |      welcome to Shabbir tool version 0.1
10011001010101001111101    |		program by MANI KAMRAN
10101011101010101010101    |   help:
01010  __________  0101    |      
0101  /          / 1101    |      -tcp => tcp config
101  /    ______/  0101    |      -udp => udp config => -TI -> for udp target ip & -TP -> for udp target recv port => this command should use after -udp command
101  \             0101    |      -i => set ip or host
1010  \____     \ 11010    |      -p => set port
01101      \     \ 1001    |      -s => save as file (TXT , CSV)
1010101011  |     |  01    |      --client => client config
1010101010  |     | 100    |      --UDPmode => set UDP mode option
101011 ____/     /  000    |      --time => time sleep to run script
1010  /         /  0101    |      --help => help menu (return this menu)  
1001  \________/  01010    |      --version => return tool version
10010            010101    |      Programmer blog : https://manikamran.blogspot.com {color.END}{color.green}
10101010100110100110011    |'''
def helpMenu():
    return f'''{color.red}
10100101000101010100101    |      welcome to Shabbir tool version 0.1
10011001010101001111101    |		program by MANI KAMRAN
10101011101010101010101    |   help:
01010  __________  0101    |      
0101  /          / 1101    |      -tcp => tcp config
101  /    ______/  0101    |      -udp => udp config => -TI -> for udp target ip & -TP -> for udp target recv port => this command should use after -udp command
101  \             0101    |      -i => set ip or host
1010  \____     \ 11010    |      -p => set port
01101      \     \ 1001    |      -s => save as file (TXT , CSV)
1010101011  |     |  01    |      --client => client config
1010101010  |     | 100    |      --UDPmode => set UDP mode option
101011 ____/     /  000    |      --time => time sleep to run script
1010  /         /  0101    |      --help => help menu (return this menu)  
1001  \________/  01010    |      --version => return tool version{color.END}{color.green}
10010            010101    |      Programmer blog : https://manikamran.blogspot.com
10101010100110100110011    |
HELP:-._____,
      |      |_._____
      |              |
      |              |_.-> -udp & --server & -p & -i example : shabbir.py --server -udp -i 127.0.0 -p 1
      |                      |
      |                      |_.-> -tcp & --server & -p & -i example : shabbir.py --server -tcp -i 127.0.0 -p 23
      |                                       |
      |                                       |_.-> --client & -tcp & -p & -i example : shabbir.py --server -tcp -i 127.0.0 -p 23
      |                                                         |
      |                                                         | + -s => shabbir.py --client\--server -tcp\-udp\  *\-U\-P *\--UDPmode -i\-p -s html/csv/txt
      |      
      |     			  
      |
      |
      |_.=> STANDARD examples :-._
            			 |       |                                    
                                 |
                                 |_.-> shabbir.py --server -udp  -f /filelocation/file.mkv -i 127.0.0 -p 23 --UDPmode [file_shear , command_shear] --time 1.min
                                 |_.-> shabbir.py --server -tcp -f file/file.file {color.END}'''



#TCP server func
def tcpServer(host,port):
    report = f'''
        Shabbir tcp server report
[*]start at {time()}'''
    def tcpServerAF_INET6(sock,IP,PORT):
        report = f'''
        Shabbir tcp server report
[*]start at {time()}'''
        try:
            helperOBJ = int(PORT)
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        try:
            sock.bind((IP,int(PORT)))
            report += f'\n[*]bind on {IP}:{PORT} at : {time()}'
            sock.listen(100)
            print(f'{color.green}[*] Listening')
            report += f'\n[*]Listening on {IP}:{PORT} at : {time()}'
            client , addr = sock.accept()
            report += f'\n[*]Accept to {addr} at : {time()}'
            try:
                while True:
                    client , addr = sock.accept()
                    report += f'\n[*]Accept to {addr} at : {time()}'
                    print(f'{color.green}[*]Waiting for client reaction : ')
                    request = client.recv(1020)
                    print(request)
                    report += f'\n[*]Recv {len(request)} bytes of data at : {time()}  |  data => {str(request)}' 
                    comamnd_send = input('Enter your command to send : ')
                    client.send(bytes(comamnd_send , 'utf-8'))
                    report + f'\n[*]Sending {len(comamnd_send)} bytes of data at : {time()}  |  data => {comamnd_send}'
            except KeyboardInterrupt:
                print(f'{color.red}[*]Program stop!!')
                report += f'\n[$]Program stop at : {time()}'
                return report
                # exit()
            except Exception as Err:
                print(f'{color.red}[*]Program stop as error!!')
                report += f'[*]An unknow Error has stoped the program at : {time}   |   Error : {Err}'
                return report
        except socket.gaierror :
            print(f'{color.red}IP is not valid Try agin!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        except OSError:
            print(f'{color.red}[*]Filed to bind some thing was wrong!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
            

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.bind((host,int(port)))
    except socket.gaierror :
        sock = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        tcpServerAF_INET6(sock,host,port)
    except ValueError:
        print(f'{color.red}[*]Can not make int of your port')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
    except OSError:
        print(f'{color.red}[*]Filed to bind some thing was wrong!!')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
    except OverflowError:
        print(f'{color.red}[*]Error port out of rang filed to bind!! rang of port => 0-65535')
        report += f'\n[$]Error at : {time()} program finished!'
        return report

        
        return report
    else:
        report += f'\n[*]bind on {host}:{port} at : {time()}'
        sock.listen(100)
        print(f'{color.green}[*] Listening')
        report += f'\n[*]Listening on {host}:{port} at : {time()}'
        client , addr = sock.accept()
        report += f'\n[*]Accept to {addr} at : {time()}'
        try:
            while True:
                print(f'{color.green}[*]Waiting for client reaction : ')
                request = client.recv(1020)
                report += f'\n[*]Recv {len(request)} bytes of data at : {time()}  |  data => {str(request)}' 
                print(request)
                comamnd_send = input('Enter your command to send : ')
                client.send(bytes(comamnd_send , 'utf-8'))
                report += f'\n[*]Sending {len(comamnd_send)} bytes of data at : {time()}  |  data => {comamnd_send}'
        except KeyboardInterrupt:
            print(f'{color.red}[*]Program stop!!')
            report += f'\n[$]Program stop at : {time()}'
            return report
            # exit()
        except  Exception as Err:
            print(f'{color.red}[*]Program stop as error!!')
            report += f'[*]An unknow Error has stoped the program at : {time}   |   Error : {Err}'
            return report

#TIME SLEEP func to --time option

def timeSleep(argv):
    try:
        time_sleep = find(r'(.+)\.(.+)',argv)
    except IndexError as e:
        print(helpMenu())
        exit()
    try:
        time = int(time_sleep[0][0])
    except ValueError:
        print(helpMenu())
        exit()
    except IndexError:
        print(helpMenu())
        exit()
    if time_sleep[0][1] in ['min','sec','hou']:
        
        if time_sleep[0][1] == 'sec':
            sleep(float(time))
        elif time_sleep[0][1] == 'min':
            sleep(float(time*60))
        elif time_sleep[0][1] == 'hou':
            sleep(float((time*60)*60))
        else:
            print(helpMenu())
            # exit()
    else:
        print(helpMenu())
        exit()
#TCP client func
def tcpClient(ip,port):
    try:
        intP = int(port)
    except ValueError:
        print(f'{color.red}[*]Can not make int of your port')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
    report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''
    def tcp_clientAF_INET6(IP,PORT):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            try:
                client.connect((IP,int(PORT)))
            except ValueError:
                print(f'{color.red}[*]Can not make int of your port')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            print(f'[*]Connect to {ip}:{port}')
            report += f'\n[*]Client connect to {IP}:{PORT} at : {time()}'
        except socket.gaierror:
            print(f'{color.red}IP is not valid Try agin!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
            # exit()
        except OSError:
            print(f'{color.red}[*]Filed to connect some thing was wrong!!')
            report += f'\n[$]Error at : {time()} program finished!'
        except OverflowError:
            print(f'{color.red}[*]Error port out of rang filed to bind!! rang of port => 0-65535')
            exit()
        try:
            while True:
                command = input ('Enter your command to send : ')
                client.send(bytes(command+'\n','utf-8'))
                report += f'\n[*]Sending {len(command)} bytes of data at : {time()}  |  data : {command}'
                print(f'{color.green}[*]Waiting for server reaction : ')
                recv = client.recv()
                report += f'\n[*]Recv {len(recv)} bytes of data at {time()}  |  data | {recv}'
        except KeyboardInterrupt:
            print('[$]Program stop!')
            report += f'\n[$]Program stop at : {time()}'
            return report
        except Exception as Err:
            print(f'{color.red}[*]Program stop as error!!')
            report += f'[*]An unknow Error has stoped the program at : {time}   |   Error : {Err}'
            return report

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        try:
            client.connect((ip,int(port)))
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        print(f'[*]Connect to {ip}:{port}')
        report += f'\n[*]Client connect to {ip}:{port} at : {time()}'

        try:
            while True:
                command = input ('Enter your command to send : ')
                client.send(bytes(command+'\n','utf-8'))
                report += f'\n[*]Sending {len(command)} bytes of data at : {time()}  |  data : {command}'
                print(f'{color.green}[*]Waiting for server reaction : ')
                recv = client.recv(1029)
                report += f'\n[*]Recv {len(recv)} bytes of data at {time()}  |  data | {recv}'
                print(recv)
        except KeyboardInterrupt:
            print('[$]Program stop!')
            report += f'\n[$]Program stop at : {time()}'
            return report
        except Exception as Err:
            print('[$]Program stop as error!!')
            report += f'[*]An unknow Error has stoped the program at : {time}   |   Error : {Err}'
            return report

    except socket.gaierror:
        tcp_clientAF_INET6(ip,port)
    except OverflowError:
        print(f'{color.red}[*]Error port out of rang filed to bind!! rang of port => 0-65535')
        exit()
    except OSError:
        print(f'{color.red}[*]Filed to connect some thing was wrong!!')
        report += f'\n[$]Error at : {time()} program finished!'
#UDP server func
def udpServer(ip,port,Tip,Tport ,mode = 'file_shear'):
    try :
        Port = int(port)
        Port = int(Tport)
    except ValueError:
        print(f'{color.red}[*]Can not make int of your port !!!')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
    if int(port) > 65535:
        print(f'{color.red}[*]Yor port was not valid !!! 0:65535')
        exit()
    if int(Tport) > 65535:
        print(f'{color.red}[*]Yor port was not valid !!! 0:65535')
        exit()
    try :
        x , helperOBJ = int(port) , int(Tport)
    except ValueError:
        print(f'{color.red}[*]Can not make int of your port')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
        
    report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''

    def UDPcommandSHEAR(port,Tip,Tport):
        def UDPcommandSHEAR_AF_INET6(port , Tip ,Tport):
            report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''
            localIP     = Tip

            try:
                localPort   = int(Tport)
            except ValueError:
                print('[*]Can not make int of your port !!')
                exit()
            try:
                bufferSize  = port
            except ValueError:
                print('[*]Can not make int of your port !!')
                exit()

            UDPServerSocket = socket.socket(family=socket.AF_INET6, type=socket.SOCK_DGRAM)

                

                # Bind to address and ip
            try:
                UDPServerSocket.bind((localIP, localPort))
            except socket.gaierror:
                print(f'{color.red}IP is not valid Try agin!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            except OSError:
                print('[*]Something was wrong try agin !!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            except PermissionError:
                print('[*]Permission denied')
                report += f'Permission denied at {time()}'
                return report
                    
            while True: 
                # Listen for incoming datagrams

                print(f'{color.green}[*]Wait for client reaction : ')


                bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

                message = bytesAddressPair[0]

                address = bytesAddressPair[1]

                clientMsg = "Message from Client:{}".format(message)
                clientIP  = "Client IP Address:{}".format(address)
                    
                print(clientMsg)
                print(clientIP)

                

                    # Sending a reply to client
                
                

                msgFromServer       = input(f'{color.green}Enter your command to send : ')

                bytesToSend         = str.encode(msgFromServer)

                UDPServerSocket.sendto(bytesToSend, address)
                
                

        report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''

        localIP     = Tip

        try:
            localPort   = int(Tport)
        except ValueError:
            print('[*]Can not make int of your port !!')
            exit()
        try:
            bufferSize  = int(port)
        except ValueError:
            print('[*]Can not make int of your port !!')
            exit()

        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

            

            # Bind to address and ip
        try:
            UDPServerSocket.bind((localIP, localPort))
        except socket.gaierror:
            UDPcommandSHEAR_AF_INET6(port = port , Tip = Tip , Tport = Tport)
            exit()
        except OSError:
            print('[*]Something was wrong try agin !!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        except PermissionError:
            print('[*]Permission denied')
            report += f'Permission denied at {time()}'
            return report
        while True: 
            # Listen for incoming datagrams
            print(f'{color.green}[*]Wait for client reaction : ')


            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            message = bytesAddressPair[0]

            address = bytesAddressPair[1]

            clientMsg = "Message from Client:{}".format(message)
            clientIP  = "Client IP Address:{}".format(address)
                
            print(clientMsg)
            print(clientIP)

            

                # Sending a reply to client
            
            

            msgFromServer       = input(f'{color.green}Enter your command to send : ')

            bytesToSend         = str.encode(msgFromServer)

            UDPServerSocket.sendto(bytesToSend, address)

        
    def UDPfileSHEAR(IP,PORT,tIP,tPORT):
        report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''
        def UDPfileSHEAR_AF_INET6(port , Tip ,Tport):
            report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''
            localIP     = Tip
            try:
                localPort   = int(Tport)
            except ValueError:
                print(f'{color.red}[*]Can not make int of your port !!!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            try:
                bufferSize  = int(port)
            except ValueError:
                print(f'{color.red}[*]Can not make int of your port !!!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report

            UDPServerSocket = socket.socket(family=socket.AF_INET6, type=socket.SOCK_DGRAM)

                

                # Bind to address and ip
            try:
                UDPServerSocket.bind((localIP, localPort))
            except socket.gaierror:
                print(f'{color.red}IP is not valid Try agin!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report 
            except OSError:
                print('[*]Something was wrong try agin !!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            except PermissionError:
                print('[*]Permission denied')
                report += f'Permission denied at {time()}'
                return report
            while True: 

                print(f'{color.green}[*]Waiting for client reaction : ')

                bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

                message = bytesAddressPair[0]

                address = bytesAddressPair[1]

                report += f'\n[*]Recv {len(message)} bytes of data at {time()}  |  data | {message}'

                fileSend = input('Enter your new file name : ')

                with open(fileSend , 'w')  as f:
                    f.write(message)
                    f.close()
                break1 = True
                while break1 == True:
                    try:
                        fileToSend = input('Enter your file to send : ')
                        sendFileOpener = open(fileToSend).read()
                        break1 = False
                    except FileNotFoundError:
                        print('Can not found your file !!!')

                bytesToSend         = str.encode(sendFileOpener)

                UDPServerSocket.sendto(bytesToSend, address)
        report = f'''
        Shabbir tcp client report
[*]start at : {time()}'''
        localIP     = Tip
        try:
            localPort   = int(Tport)
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port !!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        try:
            bufferSize  = int(port)
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port !!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report

        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

                

                # Bind to address and ip
        try:
            UDPServerSocket.bind((localIP, localPort))
        except socket.gaierror:
            print(f'{color.red}IP is not valid Try agin!')
            return report
        except OSError:
            print('[*]Something was wrong try agin !!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        except PermissionError:
            print('[*]Permission denied')
            report += f'Permission denied at {time()}'
            return report
        while True: 
            print(f'{color.green}[*]Waiting for client reaction : ')
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            report += f'\n[*]Recv {len(message)} bytes of data at {time()}  |  data | {message}'

            fileSend = input('Enter your new file name : ')

            with open(fileSend , 'w')  as f:
                f.write(message)
                f.close()
            break1 = True
            while break1 == True:
                
                try:
                    fileToSend = input('Enter your file to send : ')
                    sendFileOpener = open(fileToSend).read()
                    break1 = False
                except FileNotFoundError:
                    print('Can not found your file !!!')

            bytesToSend         = str.encode(sendFileOpener)

            UDPServerSocket.sendto(bytesToSend, address)
    if mode == 'command_shear':
        UDPcommandSHEAR(port=port , Tip=Tip , Tport = Tport)
        exit()
    elif mode  == 'file_shear':
        UDPfileSHEAR(IP=ip,PORT=port,tIP=Tip,tPORT = Tport)
        exit()
    else:
        print('[*]Filed to start your mode not fount try with : [command_shear , file_shear]')
        exit()
    
        

#UDP client
def udpClient(ip,port,Tip,Tport,mode = 'file_shear'):
    try :
        Port = int(port)
        Port = int(Tport)
    except ValueError:
        print(f'{color.red}[*]Can not make int of your port !!!')
        report += f'\n[$]Error at : {time()} program finished!'
        return report
    if int(port) > 65535:
        print(f'{color.red}[*]Yor port was not valid !!! 0:65535')
        exit()
    if int(Tport) > 65535:
        print(f'{color.red}[*]Yor port was not valid !!! 0:65535')
        exit()

    def UDPfileSHEAR(port , Tip , Tport):     
        report = f'''
    Shabbir udp client report
[*]start at : {time()}'''   
        def UDPfileSHEAR_AF_INET6(port,Tip,Tport):
            break1 = True
            while break1 == True:
                try:
                    msgFromClient       = input(f'{color.green}Enter your file : ')
                    msgFromClientF = open(msgFromClient).read()
                    break1 = False
                except FileNotFoundError:
                    print(f'{color.red}Your file not found try agin !')
                except KeyboardInterrupt:
                    print('[*]Program stoped !!')
                    return report

            bytesToSend= bytes(msgFromClientF,'utf-8')

            try:
                serverAddressPort = (Tip, int(Tport))
            except ValueError:
                print(f'{color.red}[*]Can not make int of your port !!!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report

            try:
                bufferSize          = int(port)
            except ValueError:
                print(f'{color.red}[*]Can not make int of your port !!!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report

                        

            # Create a UDP socket at client side

            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

                        

                    # Send to server using created UDP socket

            try:    
                UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            except socket.gaierror :
                print('')
                exit()
            except OSError:
                print(f'{color.red}[*]Filed to bind some thing was wrong!!')
                report += f'\n[$]Error at : {time()} program finished!'
                return report
            except PermissionError:
                print('[*]Permission denied')
                report += f'\n[$]Error at : {time()} program finished!'
                return report

            report + f'\n[*]Sending {len(bytesToSend)} bytes of data at : {time()}  |  data => {bytesToSend}'

            print(f'{color.green}[*]Wait for server reaction : ')   

            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            fileNameToSave = input('Enter your new file to send : ')
            with open(fileNameToSave,'w') as f:
                f.write(msgFromServer)
                f.close()

            report += f'\n[*]Recv {len(msg)} bytes of data at {time()}  |  data | {msg}'

        break1 = True
        while break1 == True:
            try:
                msgFromClient       = input(f'{color.green}Enter your file : ')
                msgFromClientF = open(msgFromClient).read()
                break1 = False
            except FileNotFoundError:
                print(f'{color.red}Your file not found try agin !')
            except KeyboardInterrupt:
                print('[*]Program stoped !!')
                return report

        bytesToSend= bytes(msgFromClientF,'utf-8')

        try:
            serverAddressPort = (Tip, int(Tport))
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port !!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report

        try:
            bufferSize          = int(port)
        except ValueError:
            print(f'{color.red}[*]Can not make int of your port !!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report

                    

        # Create a UDP socket at client side

        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

                    

                # Send to server using created UDP socket

        try:    
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        except socket.gaierror :
            UDPfileSHEAR_AF_INET6(port = port , Tip = Tip , Tport = Tport)
            exit()
        except OSError:
            print(f'{color.red}[*]Filed to bind some thing was wrong!!')
            report += f'\n[$]Error at : {time()} program finished!'
            return report
        except PermissionError:
            print('[*]Permission denied')
            report += f'\n[$]Error at : {time()} program finished!'
            return report

        report + f'\n[*]Sending {len(bytesToSend)} bytes of data at : {time()}  |  data => {bytesToSend}'

        print(f'{color.green}[*]Wait for server reaction : ')   

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        fileNameToSave = input('Enter your new file to send : ')
        with open(fileNameToSave,'w') as f:
            f.write(msgFromServer)
            f.close()

        report += f'\n[*]Recv {len(msg)} bytes of data at {time()}  |  data | {msg}'
        
    def UDPcommandSHEAR(port , Tip , Tport):     
        report = f'''
    Shabbir udp client report
[*]start at : {time()}'''   
        def UDPcommandSHEAR_AF_INET6(port,Tip,Tport):
            report = f'''
        Shabbir udp client report
[*]start at : {time()}'''
            while True:
                try:

                    msgFromClient       = input(f'{color.green}Enter your comamnd : ')

                    bytesToSend         = str.encode(msgFromClient)

                    serverAddressPort   = (Tip, Tport)

                    try:
                        bufferSize          = int(port)
                    except ValueError:
                        print(f'{color.red}[*]Can not make int of your port !!!')
                        report += f'\n[$]Error at : {time()} program finished!'
                        return report

                    

                    # Create a UDP socket at client side

                    UDPClientSocket = socket.socket(family=socket.AF_INET6, type=socket.SOCK_DGRAM)

                    

                    # Send to server using created UDP socket

                    
                    try:    
                        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
                    except socket.gaierror :
                        print(f'{color.red}IP is not valid Try agin!')
                        report += f'\n[$]Error at : {time()} program finished!'
                        return report
                    except OSError:
                        print(f'{color.red}[*]Filed to bind some thing was wrong!!')
                        report += f'\n[$]Error at : {time()} program finished!'
                        return report
                    except PermissionError:
                        print('[*]Permission denied')
                        report += f'\n[$]Error at : {time()} program finished!'
                        return report

                    report + f'\n[*]Sending {len(bytesToSend)} bytes of data at : {time()}  |  data => {bytesToSend}'

                    print(f'{color.green}[*]Wait for server reaction : ')

                    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
                    
                    msg = "Message from Server : {}".format(msgFromServer[0])

                    report += f'\n[*]Recv {len(msg)} bytes of data at {time()}  |  data | {msg}'

                    print(msg)
                except socket.gaierror:
                    print(f'{color.red}IP is not valid Try agin!')
                    report += f'\n[$]Error at : {time()} program finished!'
                    return report
                except KeyboardInterrupt:
                    print(f'{color.red}[*]Program stoped!')
                    return report

        while True:
            try:

                msgFromClient       = input(f'{color.green}Enter your comamnd : ')

                bytesToSend         = str.encode(msgFromClient)

                try:
                    serverAddressPort   = (Tip, int(Tport))
                except ValueError:
                    print(f'{color.red}[*]Can not make int of your port !!!')
                    report += f'\n[$]Error at : {time()} program finished!'
                    return report
                try:
                    bufferSize          = int(port)
                except ValueError:
                    print(f'{color.red}[*]Can not make int of your port !!!')
                    report += f'\n[$]Error at : {time()} program finished!'
                    return report

                

                # Create a UDP socket at client side

                UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

                

                # Send to server using created UDP socket
                
                try:    
                    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
                except socket.gaierror :
                    UDPfileSHEAR_AF_INET6(port = port , Tip = Tip , Tport = Tport)
                    exit()
                except OSError:
                    print(f'{color.red}[*]Filed to bind some thing was wrong!!')
                    report += f'\n[$]Error at : {time()} program finished!'
                    return report
                except PermissionError:
                    print('[*]Permission denied')
                    report += f'\n[$]Error at : {time()} program finished!'
                    return report
                
                report + f'\n[*]Sending {len(bytesToSend)} bytes of data at : {time()}  |  data => {bytesToSend}'

                print(f'{color.green}[*]Wait for server reaction : ')

                msgFromServer = UDPClientSocket.recvfrom(bufferSize)

                

                msg = "Message from Server : {}".format(msgFromServer[0])
                report += f'\n[*]Recv {len(msg)} bytes of data at {time()}  |  data | {msg}'

                print(msg)
            except socket.gaierror:
                UDPcommandSHEAR_AF_INET6(port,Tip,Tport)
                exit()
            except KeyboardInterrupt:
                print(f'{color.red}[*]Program stoped!')
                return report
    if mode == 'command_shear':
        UDPcommandSHEAR(port = port , Tip = Tip , Tport = Tport)
        exit()
    elif mode == 'file_shear':
        UDPfileSHEAR(port = port ,Tip = Tip , Tport = Tport)
        exit()
    else:
        print('[*]Can not found your mode !!')
        exit()
    

def update(version):
    pass