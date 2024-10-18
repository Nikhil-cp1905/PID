import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Client: {data}")
        
        # Send response to the client
        response = input("Server: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(1)
    print("Server is listening...")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} established!")

    # Start the handler in a new thread to allow full-duplex communication
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

if __name__ == "__main__":
    server_program()
