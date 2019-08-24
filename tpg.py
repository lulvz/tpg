#!/usr/bin/python3
import receiver
import hooker

#no idea if these are needed
import socket
import colorama
import subprocess

HOST = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:boqgehw31elgykialulduy6u2pzoij"
NICK = "lulascoca_bot"
CHANNEL = "#lulascoca"
buff_recv = ""

def main():

	colorama.init()

	s = socket.socket()
	a = receiver.connect_twitch(s, HOST, PORT, PASS, NICK, CHANNEL)
	if (a == 0):
		exit(0)	
	while True:
		recv = receiver.loop_recv(s)
		try:
			print(colorama.Fore.RED + recv["name"])
			print(colorama.Fore.WHITE + recv["text"] + "\n")

			if(hooker.check_focus("a")[0].decode("utf-8") == "VisualBoyAdvance\n"):
			
				if(recv["text"] == "z" or recv["text"] == "a\n"):
					hooker.loop_injector("z")
					print("sending 'z' command to visualboyadvance :)\n")
				elif(recv["text"] == "x"):
					hooker.loop_injector("x")
					print("sending 'x' command to visualboyadvance :)\n")
				elif(recv["text"] == "d"):
					hooker.loop_injector("Down")
					print("sending 'Down' command to visualboyadvance :)\n")
				elif(recv["text"] == "u"):
					hooker.loop_injector("Up")
					print("sending 'Up' command to visualboyadvance :)\n")
				elif(recv["text"] == "r"):
					hooker.loop_injector("Right")
					print("sending 'Right' command to visualboyadvance :)\n")
				elif(recv["text"] == "l"):
					hooker.loop_injector("Left")
					print("sending 'Left' command to visualboyadvance :)\n")
				elif(recv["text"] == "!enter"):
					hooker.loop_injector("Return")
					print("sending 'Return' command to visualboyadvance :)\n")

				if(recv["name"] == "lulascoca" and recv["text"] == "!esc"):
					hooker.loop_injector("Escape")
					print("quiting!\n")

			else:
				print("VisualBoyAdvance window currently not in focus loool pls wait")

		except Exception as e:
			print(e)


if __name__ == "__main__":
	main()