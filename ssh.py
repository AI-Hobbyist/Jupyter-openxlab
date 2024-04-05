# BEGIN: yz8d5f2gj3k4
import os
try:
    import paramiko
except:
    os.system("pip install paramiko")
    import paramiko
import argparse
import threading
import socket
import select

def handler(chan, host, remote_port, local_port):
    sock = socket.socket()
    try:
        sock.connect((host, local_port))
    except Exception as e:
        print('尝试转发请求到 %s:%d 失败: %r' % (host, local_port, e))
        return
    print('隧道建立成功 %r -> %r -> %r' % (chan.origin_addr,
                                                        chan.getpeername(), (host, remote_port)))
    # try:
    while True:
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
    chan.close()
    sock.close()
    print('断开连接 %r' % (chan.origin_addr,))
    # except Exception as e:
    #     print("Uncatch error",e)
    #     chan.close()
    #     sock.close()

        # return

def port_forwarding(host, username, password, port):

    remote_host = 'localhost'

    # 创建SSH客户端
    ssh = paramiko.SSHClient()

    # 自动添加主机密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(host, username=username, password=password)

    # 创建SSH传输
    transport = ssh.get_transport()

    # 创建SSH隧道

    transport.request_port_forward('', port)
    print('SSH tunnel created: {}:{}'.format(remote_host, port))
    while True:
        print('等待下一个链接')
        chan = transport.accept(1000)
        if chan is None:
            continue
        thr = threading.Thread(target=handler, args=(chan, remote_host, port, port))
        #守护线程，当程序中没有线程在运行时，就会启用垃圾回收器，回收线程，守护线程的优先级最低.
        thr.setDaemon(True)
        thr.start()
def start_as_process(host, username, password, port):
    import multiprocessing
    p = multiprocessing.Process(target=port_forwarding, args=(host, username, password, port))
    p.start()
    return p
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an SSH tunnel for port forwarding.')
    parser.add_argument('--host', type=str, help='the hostname or IP address of the SSH server')
    parser.add_argument('--username', type=str, help='the username for the SSH server')
    parser.add_argument('--password', type=str, help='the password for the SSH server')
    parser.add_argument('--port', type=int, default=0, help='the port to use for port forwarding')

    args = parser.parse_args()

    host = args.host
    username = args.username
    password = args.password
    port = args.port

    port_forwarding(host, username, password, port)
