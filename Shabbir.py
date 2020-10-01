import shabbir_moduels
from sys import argv , exit
from time import sleep
from re import findall as find
allCommands = ('-tcp','-udp','-i','-p','-s','-f','--keyFile','--server','--UDPmode','--time','--update','help','--version','--client')
tcpCommands = ('-tcp','-i','-p','-s','--server','--client','--time')
tcpCommands = ('-tcp','-i','-p','-s','--server','--client','--time','--UDPmode')
version = '0.1'
try:
    if len(argv) == 1:
        print(shabbir_moduels.menu())
        exit()
    elif len(argv) == 2:
        if argv[1] =='--help':
            print(shabbir_moduels.helpMenu())
            exit()
        elif argv[1] == '--update':
            shabbir_moduels.update(version)
        elif argv[1] == '--version':
            print(f'{shabbir_moduels.color.blue}Shabbir program Version : {version}{shabbir_moduels.color.END}')
            exit()
        else:
            print(shabbir_moduels.helpMenu())

    elif len(argv) >= 6:
        if argv[1] in allCommands:
            if argv[1] == '--server':
                if argv[2] == '-tcp':
                    if '-i' and '-p' in argv:
                        pass
                    else:
                        print(f'{shabbir_moduels.color.red}[*]Filed to ran command !')
                        print(shabbir_moduels.helpMenu())
                        exit()
                        
                    if argv[3] in tcpCommands:
                        if argv[3] == '-i':
                            try:
                                TCPhost = argv[4]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()

                            if argv[5] in tcpCommands:
                                if argv[5] == '-p':
                                    try:
                                        tcpPort = argv[6]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[7]
                                    except IndexError:
                                        outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                        if not outh == None:
                                            print(outh)
                                        exit()
                                    if argv[7] in tcpCommands:
                                            
                                        if argv[7] == '-s':
                                            try:
                                                with open(argv[8]) as f:
                                                    f.close()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[9]
                                            except IndexError:
                                                outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                with open(argv[8],'w') as f:
                                                    f.write(outh)
                                                exit()
                                            if argv[9] in tcpCommands:
                                                if argv[9] == '--time':
                                                    try:
                                                        shabbir_moduels.timeSleep(argv[10])
                                                    except IndexError:
                                                        print(shabbir_moduels.helpMenu())
                                                        exit()
                                                    outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                    if not outh == None:
                                                        print(outh)
                                                    exit()
                                                    with open(reportFileTcp , 'w') as f:
                                                        f.write(outh)
                                                    exit()
                                                    # except IndexError:
                                                    #     print(shabbir_moduels.helpMenu())            
                                                    #     exit()
                                                else:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[7] == '--time':
                                            try:
                                                shabbir_moduels.timeSleep(argv[8])
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[9]
                                            except IndexError:
                                                outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                if not outh == None:
                                                    print(outh)
                                                exit()
                                            if argv[9] in tcpCommands:
                                                if argv[9] == '-s':
                                                    try:
                                                        with open(argv[10]) as f:
                                                            f.close()

                                                        reportFileTcp = argv[10]
                                                    except FileNotFoundError:
                                                        print(shabbir_moduels.helpMenu())
                                                        exit()
                                                    except IndexError:
                                                        print(shabbir_moduels.helpMenu())
                                                        exit()
                                                    out = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                    with open(argv[10],'w') as f:
                                                        f.write(out)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())


                                    else:
                                        print(shabbir_moduels.helpMenu())                    
                                        exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                        elif argv[3] == '-p':
                            try:
                                tcpPort = argv[4]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()

                            if argv[5] in tcpCommands:
                                if argv[5] == '-i':
                                    try:
                                        TCPhost = argv[6]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[7]
                                    except IndexError:
                                        outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                        if not outh == None:
                                            print(outh)
                                        exit()
                                    if argv[7] in tcpCommands:
                                           
                                        if argv[7] == '-s':
                                            try:
                                                with open(argv[8]) as f:
                                                    f.close()

                                                
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[9]
                                            except IndexError:
                                                out = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                with open(argv[8],'w') as f:
                                                    f.write(out)
                                                exit()
                                            if argv[9] in tcpCommands:
                                                if argv[9] == '--time':
                                                    try:
                                                        shabbir_moduels.timeSleep(argv[10])
                                                    except IndexError:
                                                        print(shabbir_moduels.helpMenu())
                                                    outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                    with open(argv[8] , 'w') as f:
                                                        f.write(outh)
                                                    exit()
                                                    
                                                else:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[7] == '--time':
                                            try:
                                                shabbir_moduels.timeSleep(argv[8])
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                if not argv[9] in tcpCommands:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                            except IndexError:
                                                outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                if not outh == None:
                                                    print(outh)
                                                exit()
                                            if argv[9] == '-s':
                                                try:
                                                    with open(argv[10]) as f:
                                                        f.close()

                                                    reportFileTcp = argv[10]
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                try:
                                                    x = argv[10]
                                                except IndexError:
                                                    outh = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                    if not outh == None:
                                                        print(outh)
                                                    exit()
                                                out = shabbir_moduels.tcpServer(TCPhost,tcpPort)
                                                with open(argv[10],'w') as f:
                                                    f.write(out)
                                                exit()


                                    else:
                                        print(shabbir_moduels.helpMenu())                    
                                        exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                        else:
                            print(f'{shabbir_moduels.color.red}[*]Error to run your command in tcp option first add -p and -i then you can add other commands')
                            exit()

                    else:
                        print(shabbir_moduels.helpMenu())
                        exit()
                elif argv[2] == '-udp':
                    if argv[3] == '-i':
                        udpHost = argv[4]
                        if argv[3] in tcpCommands:
                            pass
                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                        if argv[5] == '-p':
                            udpPort = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()
                            if argv[7] == '-TI':
                                try:
                                    TI = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TP':
                                    try:    
                                        TP = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        helperOBJ = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpServer(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                        
                                        
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                
                            elif argv[7] == '-TP':
                                try:
                                    TP = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TI':
                                    try:    
                                        TI = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpServer(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                    elif argv[3] == '-p':
                        udpPort = argv[4]
                        if argv[3] in tcpCommands:
                            pass
                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                        if argv[5] == '-i':
                            udpHost = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()
                            if argv[7] == '-TI':
                                try:
                                    TI = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TP':
                                    try:    
                                        TP = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        helperOBJ = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpServer(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                        
                                        
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                
                            elif argv[7] == '-TP':
                                try:
                                    TP = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TI':
                                    try:    
                                        TI = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpServer(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpServer(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()

                                            
                                            
                                            # if argv[14] == '-s'
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()

                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                else:
                    print(shabbir_moduels.helpMenu())
                    exit()
            elif argv[1] == '--client':
                if argv[2] == '-tcp':
                    if argv[3] == '-i':
                        TCPhost = argv[4]
                        if argv[5] == '-p':
                            tcpPort = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                outh = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                if not outh == None:    
                                    print(outh)
                                exit()
                            if argv[7] == '--time':
                                try:
                                    x = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                shabbir_moduels.timeSleep(argv[8])
                                try:
                                    x = argv[9]
                                except:
                                    outh = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    if not outh == None:    
                                        print(outh)
                                    exit()
                                if argv[7] in tcpCommands:
                                    pass
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-s':
                                    try:
                                        x = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        with open(argv[10]) as f:
                                            f.close()
                                    except FileNotFoundError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    out = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    with open(argv[10],'w') as f:
                                        f.write(out)
                                    exit()
                            elif argv[7] == '-s':
                                try:
                                    x = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                try:
                                    with open(argv[8]) as f:
                                        f.close()
                                except FileNotFoundError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                try:
                                    x = argv[9]
                                except IndexError:
                                    out = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    with open(argv[8],'w') as f:
                                        f.write(out)
                                    exit()
                                if argv[9] == '--time': 
                                    try:
                                        x = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    shabbir_moduels.timeSleep(argv[10])
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                        else:
                            print(f'{shabbir_moduels.color.red}[*]Error to run your command in tcp option first add -p and -i then you can add other commands')
                            exit()

                    elif argv[3] == '-p':
                        tcpPort = argv[4]
                        if argv[5] == '-i':
                            TCPhost = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                outh = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                if not outh == None:    
                                    print(outh)
                                exit()
                            if argv[7] in tcpCommands:
                                pass
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                            if argv[7] == '--time':
                                try:
                                    x = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                shabbir_moduels.timeSleep(argv[8])
                                try:
                                    x = argv[9]
                                except:
                                    outh = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    if not outh == None:    
                                        print(outh)
                                    exit()
                                if argv[7] in tcpCommands:
                                    pass
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-s':
                                    try:
                                        x = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        with open(argv[10]) as f:
                                            f.close()
                                    except FileNotFoundError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    out = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    with open(argv[10],'w') as f:
                                        f.write(out)
                                    exit()
                            elif argv[7] == '-s':
                                try:
                                    x = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                try:
                                    with open(argv[8]) as f:
                                        f.close()
                                except FileNotFoundError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                try:
                                    x = argv[9]
                                except IndexError:
                                    out = shabbir_moduels.tcpClient(TCPhost,tcpPort)
                                    with open(argv[8],'w') as f:
                                        f.write(out)
                                    exit()
                                if argv[9] == '--time': 
                                    try:
                                        x = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    shabbir_moduels.timeSleep(argv[10])
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()

                        else:
                            print(f'{shabbir_moduels.color.red}[*]Error to run your command in tcp option first add -p and -i then you can add other commands')
                            exit()
                elif argv[2] == '-udp':
                    if argv[3] == '-i':
                        udpHost = argv[4]
                        if argv[3] in tcpCommands:
                            pass
                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                        if argv[5] == '-p':
                            udpPort = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()
                            if argv[7] == '-TI':
                                try:
                                    TI = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TP':
                                    try:    
                                        TP = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        helperOBJ = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpClient(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                        
                                        
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                
                            elif argv[7] == '-TP':
                                try:
                                    TP = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TI':
                                    try:    
                                        TI = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpClient(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()
                    elif argv[3] == '-p':
                        udpPort = argv[4]
                        if argv[3] in tcpCommands:
                            pass
                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                        if argv[5] == '-i':
                            udpHost = argv[6]
                            try:
                                x = argv[7]
                            except IndexError:
                                print(shabbir_moduels.helpMenu())
                                exit()
                            if argv[7] == '-TI':
                                try:
                                    TI = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TP':
                                    try:    
                                        TP = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        helperOBJ = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpClient(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpClientr(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()
                                        
                                        
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                
                            elif argv[7] == '-TP':
                                try:
                                    TP = argv[8]
                                except IndexError:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                                if argv[9] == '-TI':
                                    try:    
                                        TI = argv[10]
                                    except IndexError:
                                        print(shabbir_moduels.helpMenu())
                                        exit()
                                    try:
                                        x = argv[11]
                                    except IndexError:
                                        report = shabbir_moduels.udpClient(ip = udpHost , port = udpPort , Tip = TI ,Tport = TP)
                                        print(report)
                                        exit()
                                    if argv[11] == '--mode':
                                        try:
                                            mode = argv[12]
                                        except IndexError:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        if not mode in ['command_shear','file_shear']:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                        try:
                                            x = argv[13]
                                        except IndexError:
                                            report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                            print(report)
                                            exit()
                                        if argv[13] == '--time':
                                            try:
                                                x = argv[14]
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            shabbir_moduels.timeSleep(x)
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                print(report)
                                                exit()
                                            if argv[15] == '-s':
                                                try:
                                                    fileLOCation = open(argv[16],'r')
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                except FileNotFoundError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[16],'w')
                                                fileLOCation.write(report)
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        elif argv[13] == '-s':
                                            try:
                                                fileLOCation = open(argv[14],'r')
                                            except IndexError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            except FileNotFoundError:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                            try:
                                                x = argv[15]
                                            except IndexError:
                                                report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                fileLOCationOpener  = open(argv[14],'w')
                                                fileLOCation.write(report)
                                            if argv[15] == '--time':
                                                try:
                                                    x = argv[14]
                                                except IndexError:
                                                    print(shabbir_moduels.helpMenu())
                                                    exit()
                                                shabbir_moduels.timeSleep(x)
                                                try:
                                                    x = argv[15]
                                                except IndexError:
                                                    report = shabbir_moduels.udpClient(ip = udpHost , port= udpPort , Tip = TI , Tport = TP , mode = mode)
                                                    print(report)
                                                    exit()
                                            else:
                                                print(shabbir_moduels.helpMenu())
                                                exit()
                                        else:
                                            print(shabbir_moduels.helpMenu())
                                            exit()
                                                

                                            
                                    else:
                                        print('Error for udp conf first as this arg [ (1 or 2).-i  |  (1 or 2).-p  |  (2 or 3).-TI  |  (2 or 3).-TP  |  (4).--mode   |  (5 or 6).-time   |  (5 or 6).-s]')
                                        exit()

                                            
                                            
                                            # if argv[14] == '-s'
                                else:
                                    print(shabbir_moduels.helpMenu())
                                    exit()
                            else:
                                print(shabbir_moduels.helpMenu())
                                exit()

                        else:
                            print(shabbir_moduels.helpMenu())
                            exit()
                else:
                    print(shabbir_moduels.helpMenu())
                    exit()
            else:
                print(shabbir_moduels.helpMenu())
                exit()


        else:
            
            print(shabbir_moduels.helpMenu())
            exit()
    else:
        print(shabbir_moduels.helpMenu())
except KeyboardInterrupt:
    print('[*]Program stoped !')