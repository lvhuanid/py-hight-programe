import socket
# 面向对象的方法
# 实例方法、类方法、静态方法（不需要访问类的实例属性）本质是一个函数
class TcpServer:
    def __init__(self, port, tcp_server_socket=None):
        self.port = port
        self.tcp_server_socket = tcp_server_socket
        
    #__enter__
    def __enter__(self):
        print('启动with时被执行...')
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.bind(('', self.port))
        self.tcp_server_socket.listen(128)
        return self
    

    #客户端连接了服务器
    # 产生两个套接字
    #  只是负责链接的
    #  发送和接收数据的

    #获取信息
    @staticmethod
    def get_message(new_socket, client_addr):
        recv_data = new_socket.recv(1024).decode()
        print(f'{client_addr}: {recv_data}')
        # 如果客户端处于离线状态则我们的recv_data的长度为0
        if len(recv_data) == 0 or recv_data == 'exit':
            new_socket.close() # 关闭新套接字对象
            raise

    # 发送信息
    @staticmethod
    def send_message(new_socket):
        message = input('请输入你要发送的信息：').encode()
        new_socket.send(message)

    def start_server(self):
        new_socket, client_addr = self.tcp_server_socket.accept()
        while True:
            selected = int(input('请输入功能序号[1.发送信息 2.接收信息]'))
            if selected == 1:
                self.send_message(new_socket)
            elif selected == 2:
                self.get_message(new_socket, client_addr)
            else:
                print('请输入正确的序号...')
            
    # 退出方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('出现异常时被执行...')
        self.tcp_server_socket.close() # 关闭tcp连接对象

with TcpServer(8080) as tcp:
    tcp.start_server()