# For Rodney for testing.
import substitutor
import main
import testing


# inputgenerator =
# mysubstitutedinput = substitutor.Substitutor().finalEquation

mysubstitutedinput = "a + b + c"
print("Lessgooo")
generator = testing.EnglishProblemGenerator();
print(generator.generate_problem_for_equation(mysubstitutedinput))
# print(testing.generate_problem_for_equation(mysubstitutedinput))


def run_tests():
    """
    Run a series of tests to display equation output
    """

    equations = [
        # "a + b",
        "a + b + c",
        # "1 + 1 + b",
        # "a * b * c",
        # "a + b * c",
        # "a / b + c",
        # "c * g"
    ]

    for equation in equations:
        print("Original equation:")
        print(equation)

        print()
        print("Generated Problem:")
        # print(generate_problem_for_equation(equation))

        print("=============")
        print()
        print()

# for dummy_idx in range(3):
#     run_tests()