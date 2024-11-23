import socket
import time
import os
import tqdm

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
        progress = tqdm.tqdm(total=file_size, unit='B', unit_scale=True, desc="Sending")
        while True:
            bytes_read = f.read(4096)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
            progress.update(len(bytes_read))
        progress.close()

    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_speed = (file_size * 8 / elapsed_time) / (1024 * 1024) 

    print("[+] File sent successfully.")
    print("[*] Time taken: {:.2f} seconds".format(elapsed_time))
    print("[*] Average speed: {:.2f} Mbps".format(avg_speed))

    client_socket.close()

if __name__ == "__main__":
    send_file('Digits_Train.txt')


