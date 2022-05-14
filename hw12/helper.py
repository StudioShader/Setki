import socket

from random import choice
from string import ascii_uppercase

DEFAULT_GUI_TEXT_SIZE = (45, 1)

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8891

BATCH_SIZE = 2048


def random_string(n):
    return ''.join(choice(ascii_uppercase) for _ in range(n))

def gui_get():
    host, port = DEFAULT_HOST, DEFAULT_PORT
    return gui.Window('get', [
        [gui.Text('Введите IP для получения', size=DEFAULT_GUI_TEXT_SIZE), gui.InputText(host)],
        [gui.Text('Введите порт для получения', size=DEFAULT_GUI_TEXT_SIZE), gui.InputText(str(port))],
        [gui.Text('Число полученных пакетов', size=DEFAULT_GUI_TEXT_SIZE), gui.Text(key='count')],
        [gui.Text('Скорость соединения', size=DEFAULT_GUI_TEXT_SIZE), gui.Text(key='speed')],
        [gui.Button('Получить')],
    ])

def gui_send():
    return gui.Window('send', [
        [gui.Text('Введите IP для получения', size=DEFAULT_GUI_TEXT_SIZE), gui.InputText(DEFAULT_HOST, key='host')],
        [gui.Text('Введите порт для получения', size=DEFAULT_GUI_TEXT_SIZE), gui.InputText(DEFAULT_PORT, key='port')],
        [gui.Text('Введите число пакетов для отправки', size=DEFAULT_GUI_TEXT_SIZE), gui.InputText('500', key='count')],
        [gui.Button('Отправить')],
    ])

def udp_socket_init():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.settimeout(1)
    return udp_socket


def tcp_socket_init(host, port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, port))
    return tcp_socket



