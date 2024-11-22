file = 'Lotka-Volterra'

fil = open(file+'.txt', 'r')
filo = open(file+'.html', 'w')

d1 = '''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
'''

d2 = '''
</body>
</html>
'''

datos = fil.readlines()
print(len(datos))

fil.close()

p1 = '<p>'
p2 = '</p>'

filo.write(d1)

a1 = ' <a href="'
a2 = '"> '
a3 = '</a> '

k=1
for ss in datos:
  print(k)
  ss = ss.replace('\n', '')
  print(ss)
  ss1 = p1 + a1 + ss + a2+ 'link' + str(k) + a3 +  p2 + '\n'
  print(ss1)
  filo.write(ss1)
  k = k+1

filo.write(d2)
filo.close()


