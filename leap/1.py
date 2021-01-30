from typing import Dict, Optional, Tuple
import string


# Complete the max_result_expression function below.
# You may add any imports you require from the standard library.
# Feel free to define your own helper functions, classes etc as you see fit.


def max_result_expression(expression: str, variables: Dict[str, Tuple[int, int]]) -> Optional[int]:
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].

    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    output = "None"
    operands = []
    expression_list = expression.split()
    if variables == {}:
        while len(expression_list) > 0:
            temp = expression_list.pop()
            try:
                if temp not in ["+", "-", "*", "/"] and   int(temp) > 0:
                    operands.append(int(temp))
                elif temp in ["+", "-", "*", "/"]:
                    if temp == "+":
                        output = operands.pop() + operands.pop()
                        operands.append(output)
                    if temp == "-":
                        output = operands.pop() - operands.pop()
                        operands.append(output)
                    if temp == "*":
                        output = operands.pop() * operands.pop()
                        operands.append(output)
                    if temp == "/":
                        output = operands.pop() / operands.pop()
                        operands.append(output)
                    raise ValueError("Incorrect expression!")
            except ValueError as ve:
                pass

    else:
        variable = []
        while len(expression_list) > 0:
            temp = expression_list.pop()
        try:
            if temp not in ["+", "-", "*", "/"] and temp.lower() not in string.ascii_lowercase and int(temp) > 0:
                operands.append(int(temp))
            elif temp in ["+", "-", "*", "/"]:
                if temp == "+":
                    output = operands.pop() + operands.pop()
                    operands.append(output)
                if temp == "-":
                    output = operands.pop() - operands.pop()
                    operands.append(output)
                if temp == "*":
                    output = operands.pop() * operands.pop()
                    operands.append(output)
                if temp == "/":
                    output = operands.pop() / operands.pop()
                    operands.append(output)
                raise ValueError("Incorrect expression!")
        except ValueError:
            pass
    return output


if __name__ == '__main__':
    exp = str(input())
    variables = eval(input())
    res = max_result_expression(exp, variables)
    print(res)