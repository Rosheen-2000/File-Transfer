# sender.py - 运行发送端客户端
import socket
import time
import os

def send_file(file_path, host='175.27.170.205', port=80):
    # 确保文件存在
    if not os.path.isfile(file_path):
        print(f"[-] File {file_path} not found.")
        return

    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"[+] Connected to server {host}:{port}")

    file_size = os.path.getsize(file_path)
    start_time = time.time()

    # 打开文件并发送数据
    with open(file_path, 'rb') as f:
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_speed = (file_size / elapsed_time) / (1024 * 1024) * 8  # 以Mbps为单位

    print(f"[+] File sent successfully.")
    print(f"[*] Time taken: {elapsed_time:.2f} seconds")
    print(f"[*] Average speed: {avg_speed:.2f} Mbps")

    client_socket.close()

if __name__ == "__main__":
    send_file('Digits_Train.txt')
