# Author: Chanthuki Fernando
#ID : w1953817
# Date: 15th Nov 2022
# Coursework Part 01 Part 02 Part 04

pass_credit = 0  # pass credits
defer_credit = 0  # defer credits
fail_credit = 0  # fail credits
cont = "y"
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
stuDictionary= {}

while cont == "y":
    stuNum = input('Enter the student number: ')
    try:
        pass_credit = int(input("please enter your credits at pass :"))
        defer_credit = int(input("please enter your credits at defer :"))
        fail_credit = int(input("please enter your credits at fail :"))
        total_credit = pass_credit + defer_credit + fail_credit

    except ValueError:
        print("Integer required")
    else:

        if (pass_credit or defer_credit or fail_credit) not in range(0, 121, 20):
            print('Out of range')  # check if they are in range or not
            print()

        else:
            if total_credit != 120:
                print('Total incorrect')  # check total value
                print()

            else:
                if (pass_credit == 120 and defer_credit == 0 and fail_credit == 0):
                    print('Progress')  # check credit are match to the progress
                    stuDictionary[stuNum] = 'Progress',- pass_credit,defer_credit,fail_credit
                    progress_count += 1
                    print()

                elif ((pass_credit == 100 and defer_credit == 20 and fail_credit == 0) or (
                        pass_credit == 100 and defer_credit == 0 and fail_credit == 20)):
                    print('progress (module trailer)')  # check
                    stuDictionary[stuNum] = 'progress (module trailer)',- pass_credit, defer_credit, fail_credit
                    trailer_count += 1
                    print()

                elif ((pass_credit == 40 and defer_credit == 0 and fail_credit == 80) or (
                        pass_credit == 20 and defer_credit == 20 and fail_credit == 80) or (
                              pass_credit == 20 and defer_credit == 0 and fail_credit == 100) or (
                              pass_credit == 0 and defer_credit == 40 and fail_credit == 80) or (
                              pass_credit == 0 and defer_credit == 20 and fail_credit == 100) or (
                              pass_credit == 0 and defer_credit == 0 and fail_credit == 120)):
                    print('Exclude')  # check
                    stuDictionary[stuNum] = 'Exclude',- pass_credit, defer_credit, fail_credit
                    exclude_count += 1
                    print()

                else:
                    print("Do not Progress – module retriever")
                    stuDictionary[stuNum] ="Do not Progress – module retriever",- pass_credit, defer_credit, fail_credit
                    retriever_count += 1
                    print()
    finally:
        cont = input('''Would you like to enter another set of data?
    Enter 'y' for yes or 'q' to quit and view results: ''')
        cont.lower()
        if cont == "q":
            print()

            Total_histrogram = progress_count + trailer_count + retriever_count + exclude_count
            print('Histrogram\n')
            print(f"progress {progress_count :<15} : {progress_count * '*' :>1}")
            print(f"module trailer {trailer_count :<9} : {trailer_count * '*' :>1}")
            print(f"module retriever {retriever_count :<7} : {retriever_count * '*' :>1}")
            print(f"excluded {exclude_count :<15} : {exclude_count * '*' :>1}")
            print()
            print(f"{Total_histrogram} outcome in total")
            print()

            break

print("Part 4")
print()

for v, k in stuDictionary.items():
    print (v,":",k, end=" ")



