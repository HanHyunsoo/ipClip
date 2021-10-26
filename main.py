import clipboard
import socket


def my_ip_clip():
    # 네트워크에 연결되어 있는 경우
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    # 네트워크에 연결 안된 경우
    except OSError:
        return "127.0.0.1"


if __name__ == '__main__':
    clipboard.copy(my_ip_clip())
