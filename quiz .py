print('Hello, welcome to trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. what is the best programing language? ')
    if ans.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('2. what is 2 + 8 + 9 - 1 ')
    if ans.lower() == '18':
        score += 1
        print('correct')
    else:
        print('incorrect')
        

    ans = input('3. which is a better graphics card 1050ti or a 1060 ')
    if ans.lower() == '1060':
        score += 1
        print('correct')
    else:
        print('incorrect')


print('thank you for playing you got ', score, " questions correct.")
mark = (score/total_q) * 100

print("Mark: ", mark)
print('Goodbye')






        
