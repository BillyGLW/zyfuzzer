import ast

import worker_addition

def main():
	x = worker_addition.add(5, 10)
	print(x)

if __name__ == "__main__":
	main()