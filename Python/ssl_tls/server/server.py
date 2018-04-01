### On CentOS, server blocks incoming client connections by default due to firewall. Disable as below:
# service firewalld stop

### Certificate details: 

# openssl x509 -in server.crt -text -noout

### Generate a self-signed certificate: 

# openssl genrsa -des3 -out server.orig.key 2048
# openssl rsa -in server.orig.key -out server.key
# openssl req -new -key server.key -out server.csr
# openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# Ultimately, server.crt and server.key are the only ones required for tls connection.

import socket, ssl, pprint

bindsocket = socket.socket()
bindsocket.bind(('0.0.0.0', 10023))
bindsocket.listen(5)

def do_something(connstream, data):
    print "do_something:", data
    connstream.write('server says hi')
    return False

def deal_with_client(connstream):
    data = connstream.read()
    while data:
        if not do_something(connstream, data):
            break
        data = connstream.read()

while True:
    newsocket, fromaddr = bindsocket.accept()
    try:
        connstream = ssl.wrap_socket(newsocket,
                                     server_side=True,            # indicates that this is the server side
                                     cert_reqs=ssl.CERT_REQUIRED, # mandates that connecting client present its cert
                                     ca_certs="client.crt",       # client certificate to validate the client
                                     certfile="server.crt",       # server's certificate with which client validates me
                                     keyfile="server.key",        # server's private key 
                                     ssl_version=ssl.PROTOCOL_TLSv1) # Protocol. Not mandatory to specify

        # client certificate details
        print connstream.cipher()
        print pprint.pformat(connstream.getpeercert())

    except Exception as error:
        print 'Error connecting: %s' % error
        continue

    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
