import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(('', 8080))

send_message = input('请输入你要发送的数据:')
tcp_client_socket.send(send_message.encode())

recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode)

tcp_client_socket.close()