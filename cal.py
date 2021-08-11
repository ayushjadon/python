operation=input('''plz enter the arthmatic operaton:
+
-
*
/
%
**
''')
num1 = float(input('enter the first number'))
num2 =float(input('enter second number'))

if operation =='+':
    print('{}+{} ='.format(num1 , num2))
    print(num1+num2)
elif operation=='-':
    print('{} - {} ='.format(num1 , num2))
    print(num1-num2)
elif operation == '*':
     print('{}*{} ='.format(num1 , num2))
     print(num1*num2)
elif operation== '/':
    print('{}/{} ='.format(num1 , num2))
    print(num1 / num2)
elif operation=='%':
    print('{}%{}='.format(num1 ,num2))
    print(num1%num2)
elif operation=='**':
    print('{}**{}='.format(num1 ,num2))
    print(num1**num2)