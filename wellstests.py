# For Rodney for testing.
import substitutor
import main
import testing

def run_tests():
    """
    Run a series of tests to display equation output
    """

    equations = [
        # "a * b + 5",
        # "RAND[20] * RAND[20]",
        # "RAND[20] * RAND[20]",
        # "RAND[100] + RAND[50] * f",
        # "a * b + c",
        # "(a * b) + (e * f * g)",
        # "RAND[150] * (b + (k * p + n) * (1 + 2) + g) * d",
        # "a + b * c + (d * e * f)",
        # "b * c + d * e * f",
        "(a+b) /d"
    ]

    for equation in equations:
        print("Original equation:")
        print(equation)

        print()
        print("Generated Problem:")
        generator = testing.EnglishProblemGenerator(equation);
        print(generator.generate_problem_for_equation())
        # print(generate_problem_for_equation(equation))

        print("=============")
        print()
        print()


run_tests()