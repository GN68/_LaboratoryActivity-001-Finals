VALID_SEQUENCE = "<data_type> <identifier> <assignment_operator> <value> <delimiter>"

def main():
	user_input = input("Enter Tokens: ").strip()
		
	if user_input == VALID_SEQUENCE:
		print("Syntax is Correct!")
	else:
		print("Syntax is Error!")

if __name__ == "__main__":
	main()