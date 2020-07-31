def arithmetic_arranger(problems, show=False):
    
    # Rule 1
    if len(problems) > 5:
        return "Error: Too many problems."

	# Declare line variables
    rows = {
        "one": [],
        "two": [],
        "three": []
    }
    output = ""

	# Loop through giving problems and split
    for line in problems:
        line_1, operator, line_2 = line.split(" ")

		# Rule 2
        if operator == "*" or operator == "/":
            return "Error: Operator must be '+' or '-'."

		# Rule 4
        if len(line_1) > 4 or len(line_2) > 4:
            return "Error: Numbers cannot be more than four digits."

		# Rule 3
        try:
            num_1 = int(line_1)
            num_2 = int(line_2)
        except ValueError:
            return "Error: Numbers must only contain digits."
        else:
			# Main - format strings to display problems vertically
            max_len = max(len(line_1), len(line_2))
            row_width = max_len + 2

			# Format string and pad the spacing by spacing to the right via rjust
            row_1 = line_1.rjust(row_width, " ")
            row_2 = operator + " " + line_2.rjust(max_len, " ")
            row_3 = "-" * row_width

            rows["one"].append(row_1)
            rows["two"].append(row_2)
            rows["three"].append(row_3)

            if show:
                if "four" not in rows:
                    rows["four"] = []
                solution = num_1
                if operator == "+":
                    solution += num_2
                elif operator == "-":
                    solution -= num_2

                row_4 = str(solution).rjust(row_width, " ")
                rows["four"].append(row_4)

    spaces = 4
    column_spaces = " " * spaces
    rows_values = rows.values()
    for row in rows_values:
        output += column_spaces.join(row)
        output += "\n"

    return output[:-1]