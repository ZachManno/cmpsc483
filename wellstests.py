# For Rodney for testing.
import substitutor
import main
import testing


# inputgenerator =
# mysubstitutedinput = substitutor.Substitutor().finalEquation

mysubstitutedinput = "a + b + c"
mysubstitutedinput = "a * b * c + d * RAND[100]"
# print("Lessgooo")
# generator = testing.EnglishProblemGenerator(mysubstitutedinput);
# print(generator.generate_problem_for_equation())
# print(testing.generate_problem_for_equation(mysubstitutedinput))


# a * (b + c) * d

def run_tests():
    """
    Run a series of tests to display equation output
    """

    equations = [
        "a - b + c - d",
        # "a * b * c",
        # "a + b * c",
        # "RAND[100] + RAND[50] * f"
        # "a * b + c",
        # "(a * b) + (e * f * g)"
        "a * (b + c + f + g) * d",
        # "a + b * c + d * e * f",
        # "b * c + d * e * f"
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