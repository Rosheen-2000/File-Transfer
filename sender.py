import socket
import time
import os
import sys

def send_file(file_path, host='175.27.170.205', port=80):
    if not os.path.isfile(file_path):
        print("[-] File {} not found.".format(file_path))
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("[+] Connected to server {}:{}".format(host, port))

    file_size = os.path.getsize(file_path)
    client_socket.send(str(file_size).encode())

    start_time = time.time()

    with open(file_path, 'rb') as f:
        bytes_sent = 0
        while bytes_sent < file_size:
            bytes_read = f.read(10 * 1024 * 1024) 
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
            bytes_sent += len(bytes_read)

    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_speed = (file_size * 8 / elapsed_time) / (1024 * 1024) 

    print("[+] File sent successfully.")
    print("[*] Time taken: {:.2f} seconds".format(elapsed_time))
    print("[*] Average speed: {:.2f} Mbps".format(avg_speed))

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sender.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    send_file(file_path)




