import socket

def receive_file(save_path, host='localhost', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the sender.")
        
        with open(save_path, 'wb') as file:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                file.write(data)
        print("File received successfully!")

if __name__ == "__main__":
    
    save_path = r'C:\Users\DELL\Downloads\received_files\Image1.jpg' 
    receive_file(save_path)