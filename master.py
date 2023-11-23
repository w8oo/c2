import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python3 master.py "<command>" ")
    sys.exit(1)

server_list = [
    ('13.48.106.166', 80), 
    ('13.48.106.166', 80),  
    ('13.48.106.166', 80),  
    ('13.48.106.166', 80),  
]

command_to_execute = sys.argv[1]

for server_ip, server_port in server_list:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        client_socket.send(command_to_execute.encode())

        client_socket.close()

        print(f"Command sent to server {server_ip}:{server_port}")
    except Exception as e:
        print(f"Error sending command to server {server_ip}:{server_port}: {str(e)}")
