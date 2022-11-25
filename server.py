# Chihiro Asanoma
# 010960290

import socket

class Server:
  def __init__(self):
    self.balance = 100
    self.ip = "127.0.0.1"
    self.port = 7705
    self.socket_make(self.ip, self.port)

  def socket_make(self, ip, port):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((ip, port))
    self.s.listen(1)

    while True:
      print("Waiting connection...")
      conn, addr = self.s.accept()
      print("Connedted by {}".format(addr))
      optionFromClient = conn.recv(1024)
      if optionFromClient.decode() == "1":
        answer = str(self.balance)
        conn.send(answer.encode())
      if optionFromClient.decode() == "2":
        maximum = str(self.balance)
        conn.send(maximum.encode())
        money_s = conn.recv(1024)
        self.balance = self.balance - int(money_s.decode())
        message = "You have $" + str(self.balance) + " in the account"
        conn.send(message.encode())
      if optionFromClient.decode() == "3":
        message = "Enter how much do you want to deposit?"
        conn.send(message.encode())
        money_s = conn.recv(1024)
        self.balance = self.balance + int(money_s.decode())
        message = "You have $" + str(self.balance) + " in the account"
        conn.send(message.encode())

server = Server()
