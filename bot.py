import socket
import paramiko

server_ip = '0.0.0.0'  
server_port = 12345  

allowed_ip = '1.1.1.1'

def execute_ssh_command(client_address, command_to_execute):
    try:
        if client_address[0] == allowed_ip:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            private_key_path = 'path/to/your/private_key.pem'
            mykey = paramiko.RSAKey(filename=private_key_path)

            ssh.connect('hostname', username='root', pkey=mykey)

            _, stdout, stderr = ssh.exec_command(command_to_execute)

            print("Command output:")
            for line in stdout:
                print(line.strip())
            print("Command errors:")
            for line in stderr:
                print(line.strip())

            ssh.close()
            print(f"SSH command executed from {client_address[0]}")
        else:
            print(f"Request from {client_address[0]} is not allowed.")

    except Exception as e:
        print(f"Error executing SSH command: {str(e)}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Listening for incoming connections on {server_ip}:{server_port}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    command_to_execute = client_socket.recv(1024).decode()

    execute_ssh_command(client_address, command_to_execute)
    client_socket.close()
