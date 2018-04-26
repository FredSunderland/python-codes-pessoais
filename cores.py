#coding: utf-8
blue="blue"
cyan="cyan"
grey="grey"
green="green"
purple="purple"
red="red"
orange="orange"
black="black"
end="end"

def c(x):
	if x == "blue":
		return "\033[34m"
	elif x == "cyan":
		return "\033[36m"
	elif x == "grey":
		return "\033[37m"
	elif x == "green":
		return "\033[32m"
	elif x == "purple":
		return "\033[35m"
	elif x == "red":
		return "\033[31m"
	elif x == "orange":
		return "\033[33m"
	elif x == "black":
		return "\033[30m"
	elif x == "end":
		return "\033[0;0m"