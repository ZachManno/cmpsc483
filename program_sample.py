import substitutor
import readin_real
import relation_checker_utility
import testing


def run(verbose):
    # Validate integrity of data cache.
    relation_checker_utility.check()

    # Ask the user for input
    userinput = readin_real.readin_real()

    # Simplify user input
    simplifiedequation = substitutor.Substitutor().getFinalEquation(userinput)

    # Ask how many runs
    numruns = int(input("How many problems would you like for this equation?"))

    # Generate and display output.
    print("Original Equation:")
    print(simplifiedequation)
    print()
    print("Presenting " + str(numruns) + " word problems.")
    print()
    generator = testing.EnglishProblemGenerator()
    for run in range(numruns):
        print(str(run) + ".  " + generator.generate_problem_for_equation(simplifiedequation))


response = input("Verbose? Enter for no, any input for yes.")
run(len(response) > 0)