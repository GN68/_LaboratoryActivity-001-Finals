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
		"int x = 5",
		'String text = "hello;',
		"x = 5;",
		"int x;",
		"int x + 5;",
		"int x = abc;",
		"long x = abc;",
		"float x = abc;",
		"double x = abc;",
		"String text = hello;",
]


def error(msg):
	print(f"[ERROR]: {msg}")


def check(inp):
	print(inp)

	if not inp.endswith(";"):
		error("the code is missing a semicolon")
		return
	else:
		inp = inp[:-1]

	# quick string integrity check
	quotation_count = inp.count('"') + inp.count("'")
	if quotation_count % 2 != 0:
		error(
				"the code has uneven Quotation marks, please make sure to close your"
				" strings"
		)
		return

	inp = inp.replace("=", " = ")
	words = inp.split()

	if len(words) == 3 and words[1] == "=":
		error("Missing data type declaration")
		return

	if len(words) != 4:
		error("the code is Incomplete, you've forgotten to add something.")
		return

	data_type = words[0]
	value = words[3]

	if data_type == "int":
		try:
			int(value)
		except ValueError:
			error("Invalid int")
			return
	elif data_type == "long":
		clean = value
		if clean.endswith("l") or clean.endswith("L"):
			clean = clean[:-1]
		try:
			int(clean)
		except ValueError:
			error("Invalid long")
			return
	elif data_type == "float":
		clean = value
		if clean.endswith("f") or clean.endswith("F"):
			clean = clean[:-1]
		try:
			float(clean)
		except ValueError:
			error("Invalid float")
			return
	elif data_type == "double":
		clean = value
		if clean.endswith("d") or clean.endswith("D"):
			clean = clean[:-1]
		try:
			float(clean)
		except ValueError:
			error("Invalid double")
			return
	elif data_type == "char":
		if not (len(value) == 3 and value.startswith("'") and value.endswith("'")):
			error("Invalid char")
			return
	elif data_type == "String":
		if not (value.startswith('"') and value.endswith('"')):
			error("Invalid String")
			return
	elif data_type == "boolean":
		if value not in ["true", "false"]:
			error("Invalid boolean")
			return
	else:
		error(
				f'Unsupported type given: "{data_type}", only supported types are'
				" [int,long,float,double,char,String,boolean]"
		)
		return

	print("Syntax is Correct!")


def main():
	while True:
		try:
			inp = input(
					"Declare a variable: (enter nothing for a full test demo)\n"
			)
		except EOFError:
			break

		if inp:
			check(inp)
			print()
		else:
			for ex in EXAMPLES:
				check(ex)
				print()


if __name__ == "__main__":
	main()