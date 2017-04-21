import socket,os,sys;

class socketServer():
    def __init__(self):
        pass
    def socketCreate(self):
        try:

            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.host = ""
            self.port = int("")
        except socket.error, e:
            print 'Socket creation error: ' + str(e.message)
    def socketBind(self):
        try:
            print 'Binding socket at port %s' % (self.port)
            self.s.bind(self.host,self.port)
            self.s.listen(1)
        except socket.error, e:
            print 'Socket binding error: ' + str(e.message)
            print 'Retrying...'
            self.socketBind()
