def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    answers = []
    max_lengths = []

    for problem in problems:
        parts = problem.split()

        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        max_lengths.append(max(len(first_operand), len(second_operand)) + 2)

        if operator == '+':
            answers.append(str(int(first_operand) + int(second_operand)))
        else:
            answers.append(str(int(first_operand) - int(second_operand)))

    arranged_problems = []

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i in range(len(problems)):
        first_line += first_operands[i].rjust(max_lengths[i]) + '    '
        second_line += operators[i] + second_operands[i].rjust(max_lengths[i] - 1) + '    '
        dashes_line += '-' * max_lengths[i] + '    '
        if display_answers:
            answers_line += answers[i].rjust(max_lengths[i]) + '    '

    arranged_problems.append(first_line.rstrip())
    arranged_problems.append(second_line.rstrip())
    arranged_problems.append(dashes_line.rstrip())
    if display_answers:
        arranged_problems.append(answers_line.rstrip())

    return '\n'.join(arranged_problems)

# Example function call

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
