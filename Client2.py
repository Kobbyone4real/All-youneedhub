import socket
server = "192.168.44.130"
port = 8888
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect ((server,port))
input_str = client_socket.recv(1024).decode().split(" ")
print(input_str[0])
input_str[0] = input_str[0].lower()
if input_str[0] == "HELLO":
	client_socket.send('hello acheampong.k\n'.encode())
	while True :
		input_str = client_socket.recv(1024).decode().split(" ")
		#print(input_str)
		if input_str[0] == "MATH":
			res = 0
			a = int(input_str[1])
			b = int(input_str[3])
			if input_str[2] == "+":
				res = a+b
			if input_str [2] == "-":
				res = a-b
			if input_str [2] == "*":
				res = a*b
			if input_str [2] == "//":
				res = a//b
			print(res)
			sendans = "ANSWER " + str(res) + "\n"
			client_socket.send(sendans.encode())
		if input_str[0] == "DONE":
			print("Your flag is " + input_str[1])
			break
		if input_str[0] == " ":
			break

client_socket.close()
