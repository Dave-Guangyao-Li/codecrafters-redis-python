# Uncomment this to pass the first stage
import socket
# Uncomment this to pass the first stage
server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
server_socket.accept() # wait for client