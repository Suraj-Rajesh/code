import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s,
                           certfile="client.crt",   # client's cert presented to the server for validation
                           keyfile="client.key",    # client's key required along with the server's
                           ca_certs="server.crt",   # server's cert to validate when client makes a connection
                           cert_reqs=ssl.CERT_REQUIRED) # mandates that server present its cert for https

ssl_sock.connect(('192.168.98.190', 10023))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

ssl_sock.write("client data")
print ssl_sock.read()

if False: # from the Python 2.7.3 docs
    # Set a simple HTTP request -- use httplib in actual code.
    ssl_sock.write("""GET / HTTP/1.0r
    Host: www.verisign.comnn""")

    # Read a chunk of data.  Will not necessarily
    # read all the data returned by the server.
    data = ssl_sock.read()

    # note that closing the SSLSocket will also close the underlying socket
    ssl_sock.close()

