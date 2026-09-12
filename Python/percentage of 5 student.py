#Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 =int (input ( 'enter  marks of subject 1'))
sub2= int (input('enter marks of subject 2'))
sub3 = int  (input('enter marks of subject3'))
sub4= int (input ('enter marks of subject 4'))
sub5= int(input ('enter marks of subject 5'))

total = sub1+sub2+sub3+sub4+sub5
percentage =(total/500 * 100)

print("total marks =", total)
print ('percentage =',percentage) 