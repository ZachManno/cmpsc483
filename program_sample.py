import substitutor
import readin_real
import relation_checker_utility
import testing


def run(verbose):
    # Validate integrity of data cache.
    relation_checker_utility.check(verbose)

    # Ask the user for input
    simplifiedequation = substitutor.Substitutor().finalEquation

    print("You provided the following equation: ")
    print(simplifiedequation)

    # Ask how many runs
    numruns = int(input("How many problems would you like for this equation?"))

    # Generate and display output.
    print("Original Equation:")
    print(simplifiedequation)
    print()
    print("Presenting " + str(numruns) + " word problems.")
    print()
    generator = testing.EnglishProblemGenerator(simplifiedequation)
    for run in range(numruns):
        print(str(run + 1) + ".  " + generator.generate_problem_for_equation())


response = input("Verbose? Enter for no, any input for yes.")
run(len(response) > 0)