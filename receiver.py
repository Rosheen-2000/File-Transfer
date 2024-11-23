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

        # 打开一个文件用于写入接收到的数据
        with open('received_file.txt', 'wb') as f:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                f.write(data)

        print(f"[+] File received from {addr}")
        client_socket.close()

if __name__ == "__main__":
    start_server()
