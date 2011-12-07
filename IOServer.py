#!/usr/bin/python


import socket
import threading
import SocketServer

#initial program setup

def get_config():
    c = {'nodes':[],
         'paths':{}}
    n = {'name':'wellhouse',
         'ip':'172.17.17.50',
         'port':37826}
    c['nodes'].append(n)
    return c


#main


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

   # def handle(self):
        #data = self.request.recv(1024)
        #cur_thread = threading.currentThread()
        #response = "%s: %s" % (cur_thread.getName(), data)
        #print response
        #self.request.send(response)
    def handle(self):
        data = self.request.recv(1024)
        if(self.parse_data(data)):
            self.request.send('ok')
        else:
            selef.request.send('fail')

    def parse_data(self,data):
        msg_len = int(data[:4])
        msg = data[4:]
        print data
        if len(msg) == msg_len:
            return True
        else:
            return False

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


    
#program cleanup


#reload config


#if __name__ == '__main__':
    #config = get_config()
    #print repr(config)
if __name__ == "__main__":
    HOST, PORT = "localhost", 1032

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print ip

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    #server_thread.setDaemon(True)
    server_thread.start()
    print "Server loop running in thread:", server_thread.getName()

    #block until keyboard input
    inp = raw_input()
    server.shutdown()


