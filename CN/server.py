import socket

def send_file(file_path, host='localhost', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Waiting for connection...")
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                conn.sendall(data)        
        print("File sent successfully!")
        conn.close()

if __name__ == "__main__":
    file_path = r'D:\SIH\WhatsApp Image 2024-08-22 at 00.00.16_adacbb14.jpg' 
    send_file(file_path)
