#!/usr/bin/python3
import socket

def connect_twitch(s, HOST, PORT, PASS, NICK, CHANNEL):
	try:
		s.connect((HOST, PORT))
		s.send(("PASS " + PASS + "\r\n").encode("utf-8"))
		s.send(("NICK " + NICK + "\r\n").encode("utf-8"))
		s.send(("JOIN " + CHANNEL + "\r\n").encode("utf-8"))
		return 1
	except:
		print("error connecting to twitch....")
		return 0

def loop_recv(s):
	buff_recv = s.recv(1024).decode("utf-8")
	name_sender = buff_recv.split("!")[0]
	buff_recv = buff_recv.split("\n")[0]

	try:
		temp = buff_recv.split(":", 2)[2].split("\r")
		final_str = temp[0]
		final_name = name_sender.split("\n")[0]
		return {"name": final_name, "text": final_str}

	except:
		return None

def main():

	HOST = "irc.twitch.tv"
	PORT = 6667
	PASS = "oauth:boqgehw31elgykialulduy6u2pzoij"
	NICK = "lulascoca_bot"
	CHANNEL = "#jakenbakelive"
	buff_recv = ""

	s = socket.socket()
	if(connect_twitch(s, HOST, PORT, PASS, NICK, CHANNEL)):
		while True:
			recv = receiver.loop_recv(s)
			try:
				print(recv["name"] + "\n" + recv["text"])
			except:
				pass

if __name__ == "__main__":
	main()