# receiver.py - 运行接收端服务器
import socket
import sys

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

        received_size = 0
        # 打开一个文件用于写入接收到的数据
        with open('received_file.txt', 'wb') as f:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                f.write(data)
                received_size += len(data)
                # 打印简单的进度信息
                progress = (received_size / file_size) * 100
                sys.stdout.write(f"\rReceiving: {progress:.2f}%")
                sys.stdout.flush()

        print(f"\n[+] File received from {addr}")
        client_socket.close()

if __name__ == "__main__":
    start_server()



