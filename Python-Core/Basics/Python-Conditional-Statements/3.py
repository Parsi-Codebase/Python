#nested-if
a=110
b=220
c=30
if a>b:
    if a>c:
     print('a is bigger')
    else:
       print('c is bigger')
else:
    if b>c:
      print('b is bigger')
    else:
      print('c is bigger')