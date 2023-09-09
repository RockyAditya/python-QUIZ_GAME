print('Welcome to  Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 5
if answer.lower()!='yes':
     answer = print("Thanks come again")
     exit(0)


if answer.lower() == 'yes':
    answer = input(
        'Question 1: What is your Favourite programming language?\n 1) python \n 2) java \n 3) c\nyour Answer : ')

    if answer.lower() == '1' or '2' or '3':

        print('ok')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬 ')
        print("--------------------------------------------------------------------------------------------")

if answer.lower() == '1':
    answer = input(
        'Question 2: who created python ?\n a)guido van rossum \n b)james gause \n c)dennis ritche \n your ans : ')
    if answer.lower() == 'a':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => guido van rossum was created the python ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 3: How to save a file in python ?\n a).py \n b).pipy \n c).pi \n your ans : ')
    if answer.lower() == 'a':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => .py is used to save the python file ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 4: How to add comment in python ?\n a)// \n b)/ \n c)# \n your ans : ')

    if answer.lower() == 'c':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => # is used to add comment to a program  ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 5: What is the basic data type for storing numbers in Python ? \n a) int, double, String \n b) int, '
        'float, complex \n c) int, float, double \n your ans : ')

    if answer.lower() == 'b':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => int, float, complex are the types used to store numbers in python ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 6:Which type of Programming does Python support? \n a) object-oriented programming \n b) structured '
        'programming \n c) functional programming \n d) all of the mentioned \n your ans : ')

    if answer.lower() == 'd':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => Python is an interpreted programming language, which supports object-oriented, '
              'structured, and functional programming.  ')
        print("--------------------------------------------------------------------------------------------")

if answer.lower() == '2':
    answer = input(
        'Question 2: Who invented Java Programming ?\n a)guido van rossum \n b)james Gosling \n c)dennis ritche \n '
        'your ans : ')
    if answer.lower() == 'b':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer =>  Java programming was developed by James Gosling at Sun Microsystems in 1995. James '
              'Gosling is well known as the father of Java. ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 3: Which statement is true about Java ?\n a)Java is a sequence-dependent programming language \n '
        'b)Java is a platform-dependent programming language \n c)Java is a platform-independent programming language '
        '\n d) Java is a code dependent programming language \n your ans : ')
    if answer.lower() == 'c':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => Java is called ‘Platform Independent Language’ as it primarily works on the principle '
              'of ‘compile once, run everywhere')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 4:  Which component is used to compile, debug and execute the java programs ?\n a)JVM \n b)JRE \n '
        'c)JDK \n d) JIT \n your ans : ')
    if answer.lower() == 'c':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => JDK is a core component of Java Environment and provides all the tools, executables '
              'and binaries required to compile, debug and execute a Java Program.')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 5: What is the extension of java code files ?\n a).java \n b).Js  \n '
        'c).txt \n d).class \n your ans : ')
    if answer.lower() == 'a':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer =>  Java files have .java extension.')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 6:  Which of these keywords is used to define interfaces in Java? \n a) intf \n b) interface \n c) '
        'Intf \n d)Interface \n your ans : ')
    if answer.lower() == 'b':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => interface keyword is used to define interfaces in Java.')
        print("--------------------------------------------------------------------------------------------")

if answer.lower() == '3':
    answer = input(
        'Question 2: Who invented c ?\n a)steve jobs \n b)james Gosling \n c)dennis ritchie \n '
        'your ans : ')
    if answer.lower() == 'c':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => Dennis Ritchie is the father of C Programming Language. C programming language was '
              'developed in 1972 at American Telephone & Telegraph Bell Laboratories of USA. ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 3:  Which of the following is not a valid C variable name?\n a)int number; \n b)float rate; \n '
        'c)int variable_count; \n d) int $main; \nyour ans : ')
    if answer.lower() == 'd':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => Since only underscore and no other special character is allowed in a variable name, '
              'it results in an error. ')
        print("--------------------------------------------------------------------------------------------")

    answer = input(
        'Question 4:  What is an example of iteration in C? \n a) for \n b) while \n '
        'c) do-while \n d) all of the mentioned \n your ans : ')
    if answer.lower() == 'd':
        score += 1
        print('Correct ✌️')
        print("--------------------------------------------------------------------------------------------")
    else:
        print('Wrong Answer :( 😬')
        print('correct answer => all the mentioned are iterations in c')
        print("--------------------------------------------------------------------------------------------")

print(' Thanks for playing the small quiz 👌', score, " questions correctly answered! ")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('BYE! 👋')
