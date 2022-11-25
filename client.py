# Chihiro Asanoma
# 010960290

import socket

class Client:
  def __init__(self):
    self.server_ip = "127.0.0.1"
    self.server_port = 7705
    self.socket_make(self.server_ip, self.server_port)

  def socket_make(self, ip, port):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect((ip, port))

client = Client()
while True:
  print("1. Check the available balance 2. Withdraw money from the account 3. Deposit money into the account 4. Disconnect")
  x = input("Choose your option: ")
  x = int(x)
  if x == 1:
    option = "1"
    client.s.send(option.encode())
    balance = client.s.recv(1024)
    print("You have $" + balance.decode() + " in the account")
    print("")
    Client.socket_make(client, client.server_ip, client.server_port)
  if x == 2:
    option = "2"
    client.s.send(option.encode())
    maximum = client.s.recv(1024)
    maximum_i = int(maximum.decode())
    while True:
      withdraw = input("Enter how much do you want to withdraw?: $")
      if not withdraw.isdigit():
        print("please enter number")
      elif int(withdraw) > int(maximum_i):
        print("You are trying to withdraw more than you have")
      else:
        break
    client.s.send(withdraw.encode())
    info = client.s.recv(1024)
    print(info.decode())
    print("")
    Client.socket_make(client, client.server_ip, client.server_port)
  if x == 3:
    option = "3"
    client.s.send(option.encode())
    message = client.s.recv(1024)
    while True:
      deposit = input(message.decode() + ": $")
      if not deposit.isdigit():
        print("please enter number")
      else:
        break
    client.s.send(deposit.encode())
    info = client.s.recv(1024)
    print(info.decode())
    print("")
    Client.socket_make(client, client.server_ip, client.server_port)
  if x == 4:
    print("Disconnect")
    break


print("Bye")