import requests
import socket
def main():
    url = "http://ip.wang-li.top:93/4u6385IP"
    MyIP = requests.get(url).text
    print('internetIP', MyIP)


if __name__ == '__main__':
    print('localIP', socket.gethostbyname(socket.getfqdn(socket.gethostname())))
    main()