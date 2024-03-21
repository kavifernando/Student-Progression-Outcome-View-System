#Author: Chanthuki Fernando
#Date: 15th Nov 2022
#Coursework Part 01 Part 02 Part 03

pass_credit = 0   #pass credits
defer_credit = 0  #defer credits
fail_credit = 0   #fail credits
cont = "y"
progressSet1 =[]
moduleTrailer = []
excludeSet = []
moduleRetriever = []
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0


while cont=="y":
    try:
        pass_credit = int(input("please enter your credits at pass :"))
        defer_credit = int(input("please enter your credits at defer :"))
        fail_credit = int(input("please enter your credits at fail :"))
        total_credit = pass_credit + defer_credit + fail_credit

    except ValueError:
        print ("Integer required")
    else:
        
        if(pass_credit or defer_credit or fail_credit) not in range(0,121,20):
            print('Out of range') # check if they are in range or not
            print()
            
        else:
            if total_credit != 120:
                print('Total incorrect')# check total value
                print()
                
            else:
                if(pass_credit == 120 and defer_credit == 0 and fail_credit == 0 ):
                    print('Progress') #check credit are match to the progress
                    credit1 = str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)
                    progressSet1.append(credit1)
                    progress_count += 1
                    print()
                    
                elif((pass_credit == 100 and defer_credit == 20 and fail_credit == 0) or (pass_credit ==100 and defer_credit == 0 and fail_credit == 20)):
                    print('progress (module trailer)')# check
                    credit2 = str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)
                    moduleTrailer.append(credit2)
                    trailer_count += 1
                    print()
                    
                elif((pass_credit == 40 and defer_credit == 0 and fail_credit == 80) or (pass_credit == 20 and defer_credit == 20 and fail_credit == 80) or (pass_credit == 20 and defer_credit == 0 and fail_credit == 100) or (pass_credit == 0 and defer_credit == 40 and fail_credit == 80) or (pass_credit == 0 and defer_credit == 20 and fail_credit == 100) or (pass_credit == 0 and defer_credit == 0 and fail_credit == 120)):
                    print('Exclude')#check
                    credit3 = str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)
                    excludeSet.append(credit3)
                    exclude_count += 1
                    print()
                    
                else:
                    print("Do not Progress – module retriever")
                    credit4 = str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)
                    moduleRetriever.append(credit4)
                    retriever_count += 1
                    print()
    finally:
        cont= input('''Would you like to enter another set of data?
    Enter 'y' for yes or 'q' to quit and view results: ''')
        cont.lower()
        if cont == "q":
            print()
            
            Total_histrogram = progress_count + trailer_count + retriever_count + exclude_count
            print('Histrogram\n')
            print(f"progress {progress_count :<15} : {progress_count *'*' :>1}")
            print(f"module trailer {trailer_count :<9} : {trailer_count *'*' :>1}")
            print(f"module retriever {retriever_count :<7} : {retriever_count *'*' :>1}")
            print(f"excluded {exclude_count :<15} : {exclude_count *'*':>1}")
            print()
            print(f"{Total_histrogram} outcome in total")
            print()
            
            for i in progressSet1: 
                print ("Progress -",i)
            for i in moduleTrailer:
                print("progress (module trailer) -",i)
            for i in excludeSet:
                print("Exclude -",i)
            for i in moduleRetriever:
                print("Module Retriever -",i)
                
            break

file = open('textfile.txt','a+')
for i in progressSet1:
    value = "progress - "+str(i)+"\n"
    file.write(value)

for i in moduleTrailer:
    value = "progress (module trailer) - "+str(i)+"\n"
    file.write(value)

for i in excludeSet:
    value = "exclude - "+str(i)+"\n"
    file.write(value)

for i in moduleRetriever:
    value = "module retriever - "+str(i)+"\n"
    file.write(value)
file.close()

file = open('textfile.txt','r')
with file:
    print()
    print('part 3:')
    print()
    file = file.read()
    print(file)
        
    
    
