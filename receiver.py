# receiver.py - 运行接收端服务器
import socket

def start_server(host='0.0.0.0', port=80):
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] Accepted connection from {addr}")

        # 接收文件大小信息
        file_size = client_socket.recv(1024).decode()
        file_size = int(file_size)

        # 打开一个文件用于写入接收到的数据
        with open('received_file.txt', 'wb') as f:
            bytes_received = 0
            while bytes_received < file_size:
                data = client_socket.recv(10 * 1024 * 1024)  # 每次接收 10MB
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)

        print(f"[+] File received from {addr}")
        client_socket.close()

if __name__ == "__main__":
    start_server()


