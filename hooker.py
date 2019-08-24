#!/usr/bin/python3
import subprocess

def check_focus(window):
	bash_check = "xdotool getwindowfocus getwindowname"	# requiers xdotool
	process = subprocess.Popen(bash_check.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	return (output, error)

def loop_injector(key):
	if key == "Up" or key == "Down" or key == "Right" or key == "Left" or key == "z" or key == "x" or key == "Return" or key == "Escape":
		process = subprocess.Popen("xdotool key {}".format(key), stdout=subprocess.PIPE, shell=True)
		output, error = process.communicate()

def main():
	keyboard = kb.Controller()

	while(1):
		if (check_focus("a")[0].split("\n").decode("utf-8") == "./hooker.py"):
			pass

if __name__ == "__main__":  
	main()