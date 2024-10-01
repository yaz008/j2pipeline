from socket import socket as Socket
from threading import Thread
from dataclasses import dataclass
from typing import Callable

@dataclass(slots=True)
class Client:
    socket: Socket

    def send(self, message: str) -> str:
        data: bytes = message.encode(encoding='UTF-8')
        size: bytes = f'{len(data):16}'.encode(encoding='UTF-8')
        self.socket.send(size)
        self.socket.send(data)
        while True:
            size: int = int(self.socket.recv(16).decode(encoding='UTF-8').strip())
            message: str = self.socket.recv(size).decode(encoding='UTF-8')
            return message

    def close(self) -> None:
        self.socket.close()