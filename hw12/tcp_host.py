import datetime

import PySimpleGUI as gui

import helper
from helper import *

window = helper.gui_send()

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == 'Отправить':
        host, port, messages_count = None, None, 0
        try:
            host, port = values['host'], int(values['port'])
            messages_count = int(values['count'])
        except Exception as e:
            print(e)

        tcp_socket = None
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.connect((host, port))
            tcp_socket.sendall(bytes(str(messages_count), encoding='utf-8'))
            for i in range(messages_count):
                message = f'{int(datetime.datetime.now().timestamp() * 1000)} '
                message = random_string(BATCH_SIZE - len(message))
                tcp_socket.sendto(message.encode(), (host, port))
        except Exception as e:
            print(e)
        finally:
            if tcp_socket is not None:
                tcp_socket.close()
