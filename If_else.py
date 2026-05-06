a1=int(input('Enter the age of  1st person : '))
a2=int(input('Enter the age of  2nd person : '))
a3=int(input('Enter the age of  3rd person: '))
if (a1>a2 and a1>a3):
 print('1st is elder')
elif(a2>a1 and a2>a3):
    print('2nd is elder')
elif(a3>a1 and a3>a2):
    print('3rd is elder')
else :
     print('Any two are same and one is diffrent')



- Output (example):

Enter the age of 1st person: 20  
Enter the age of 2nd person: 25  
Enter the age of 3rd person: 22



2nd is elder
