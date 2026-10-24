import re

EXAMPLES = [
	# CORRECT SET
	"int x = 5;",
	"long num = 10L;",
	"float fl = 1.2f;",
	"double db = 3.14;",
	"char ch = '7';",
	'String text = "hello";',
	"boolean flag = true;",

	# INVALID SET
	"int x = 5",# 1. "the code is missing a semicolon"
	'String text = "hello;',# 2. "the code has uneven Quotation marks..."
	"x = 5;",# 3. "Missing data type declaration"
	"int x;",# 4. "the code is Incomplete, you've forgotten to add something."
	"int x + 5;",# 5. "Unexpected token..."
	"int x = abc;",# 6. "Invalid int"
	"long x = abc;",# 7. "Invalid long"
	"float x = abc;",# 8. "Invalid float"
	"double x = abc;", # 9. "Invalid double"
	"String text = hello;",# 10. "Invalid String"
]

def error(msg):
	print(f"[ERROR]: {msg}")

def check(input_str):
	print(input_str)

	# check semicolon
	if not input_str.endswith(";"):
		error("the code is missing a semicolon")
		return
	else:
		input_str = input_str[:-1]

	# check quotation marks
	quotation_count = input_str.count('"') + input_str.count("'")
	if quotation_count % 2 != 0:
		error("the code has uneven Quotation marks, please make sure to close your strings")
		return

	# serialize string
	input_str = input_str.replace("=", " = ")
	words = input_str.split()

	# missing data type declaration
	if len(words) == 3 and words[1] == "=":
		error("Missing data type declaration")
		return

	# incomplete declaration
	if len(words) != 4:
		error("the code is Incomplete, you've forgotten to add something.")
		return

	data_type = words[0]
	assignment = words[2]
	value = words[3]

	if assignment != "=":
		error(f'Unexpected token "{assignment}", it should be "="')
		return

	if data_type == "int":
		if not re.match(r"^[+-]?\d+$", value):
			error("Invalid int")
			return
	elif data_type == "long":
		if not re.match(r"^[+-]?\d+[lL]?$", value):
			error("Invalid long")
			return
	elif data_type == "float":
		if not re.match(r"^[+-]?(\d+|\d+\.\d+|\.\d+|\d+\.)([eE][+-]?\d+)?[fF]?$", value):
			error("Invalid float")
			return
	elif data_type == "double":
		if not re.match(r"^[+-]?(\d+|\d+\.\d+|\.\d+|\d+\.)([eE][+-]?\d+)?[dD]?$", value):
			error("Invalid double")
			return
	elif data_type == "char":
		if not re.match(r"^'.'$", value):
			error("Invalid char")
			return
	elif data_type == "String":
		if not (value.endswith('"') and value.startswith('"')):
			error("Invalid String")
			return
	elif data_type == "boolean":
		if value not in ["true", "false"]:
			error("Invalid boolean")
			return
	else:
		error(f'Unsupported type given: "{data_type}", only supported types are [int,long,float,double,char,String]')
		return

	print("Syntax is Correct!")

def main():
	while True:
		try:
			user_input = input("Declare a variable: (enter nothing for a full test demo)\n")
		except EOFError:
			break

		if user_input.strip() != "":
			check(user_input)
			print()
		else:
			for ex in EXAMPLES:
				check(ex)
				print()

if __name__ == "__main__":
	main()