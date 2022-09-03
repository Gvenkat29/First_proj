"""x =2
y =8
#print(x,y,sep='---')
print(x, end=' ')
print(y)

print ('.................////////')

a = 4
b = 9
print(a,b, sep='...>>')
print ('%d'%(a))
print('%d'%(b))
print('%d\t%d'%(a,b))

p = 21.35
r = 42.11
print (p,r,sep='>>>')
print (p,end=' ')
print (r)
print ('%f'%(p))
print ('%f\t%f'%(p,r))
print ('%.2f'%(p))
print ('%.1f'%(r))

print (132&92)
print (48|28)
print (10<<23)
print (10>>3) 


def sum(a, b):
    return a + b 


add = sum(5, 8)
print(add) """


def f1():
    
    print ('satya')
    f2()
    #print('ravi')


def f2():
    print('hey')
    f1()
#f2()
print('......')


num = 5
for x  in range (1,11):
    print (num, 'X', x, '=', num * x, end=' ' )


nam = 'name'
for i in range(1,11):
    print (nam)


for j in range(65,91):
    print (chr(j),end=' ')
    
print ('\n...........')

for a in range(97,123):
    print(chr(a), end=' ')
    
print('\n............')

for r in range(65,91):      #  122+65
    print(chr(r), '--', chr(187-r))

print ('............................////')
# while else loop...

no = 23
ans = 0
while no != 0:
    rem1 = no % 10
    no = no // 10
    
    ans = ans * 10 + rem1

else:
    print('reverse num is: ',ans)


print('.......................//////')


ans = 0
no = int(input('enter num: '))

while no != 0:
    
    rem1 = no % 10
    no = no // 10    
    ans =  ans + rem1

else:
    print('reverse num is: ',ans)


print('.........................../////')

s2 = 'venk32at43'
result = ''
for x in s2:
    if x.isalpha():
        result += x
print('Only alpha: ', result)

print('......................../////')

print(dir(dict))
print(dict.update.__doc__)

['clear', 'copy', 'fromkeys', 'get', 'items',
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print('..............................//////')

"""def add(idn,name=0,*args,**kwargs):
    print(idn)
    print(name)
    print(*args)
    print(**kwargs)

add(10,'venkat',2,5,4,6,value=12,age=35)"""



#print(dir(str))
#print(str.isalnum.__doc__)


n = 'coding'
cunt = 0
for i in n:
    cunt += 1
    if cunt == 1:
        print('value: ', i, '-', cunt)
        
    else:
        print('choice..')

print('......................../////')


'''username = ['ravi','joythi', 'kamala', 'suda']
password = ['jai', 'bheem', 'giri', 'just']

uname = input('enter usr name: ')
pswd = input('enter pswd: ')

if uname in username:
    pos = username.index(uname)
    print(pos)
    if pswd == password[pos]:
        print('validate', uname, pswd)'''


import sys
import os
import re

import random

r = random.randint(1,112)
print(r)

rc = random.choice('Naveen kumar')
rt = random.choice(['ravi', 'janu', 'kajal'])
rlst = random.choice([21,54,84,71])

print(rc)
print(rt)
print(rlst)

choice = ['ravi', 'janu', 'kajal']
random.shuffle(choice)
print(choice)


print('......................../////')

dcr = {21:'baby', 32:'sarayu', 42:'janaki'}
print(dcr)

print(dcr.keys())   # return in list
print(dcr.values())
print(dcr.items())

default = dcr.setdefault(22)
print(default)
print(dcr)
print(dcr[22])

print('......................../////')

val = [21,54,[48,52],84,71]

for v in val:
    #print(v)

    if isinstance(v, list):
        #print('indx is: ', val.index(v))
        continue
    print(v, end=' ')

print('......................../////')

#
var= "James Bond"
print(var[2::-1])

import re
def str_to_list( str ) :
	r = re.findall('\S', str)
	print(list(r))
str_to_list('my string')

print('......................../////')

# Files.

pat = 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\code.txt'

print(pat)


p = open(pat,'a')
r = p.write('\nthis is checking.')

p.close()

print(r)

 
pp = open(pat)
rr = pp.read()
print(rr)

pp.close()
print(pp.closed)
print(pp.name)

print('.........+++++.......')

with open(pat, 'r+') as op:
    rd = op.write('\nhey! this r+ mode not r mode.')
    print(type(rd))
    
    print(op.writable())
    print(op.readable())
    print(type(op))
    
    
    #print(op.seek(21))

    #for j in rd:
        #print(j,end='')

print('......................../////')

# re.

search = 'jiamalini is that@ great# actor? u know'
print(search)

m = re.match('ji', search)
f = re.findall('\s', search)

print(f)
#print(m)

s = re.findall('\w+', search)
print(s)



pat_one = 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\'

ndir = 'just_code'

#npt = os.mkdir(pat_one + ndir)

#print(npt)

npat = os.path.join(pat_one + ndir)
print(npat)

dir_inf = os.listdir(npat)
print(len(dir_inf))


w_inf = os.walk(pat_one)

#for j in w_inf:
 #   print(j.name())


print('......................../////')

# try.

try:
    print(20/0)
    
except:
    print('check given val.')


n = 1
while  n == 0:
    print('not zero')
    
else:
    print('zero.')


for i in range(3):
    print(i)
    
else:
    print('check range')


sample = 'python'
print(sample)

print(sample[2])

#sample[2] = 'h'
#print(sample)

print('......................../////')


dsk_pat = 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\nez.txt'
print(dsk_pat)


#rnm = os.rename(dsk_pat, 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\nez.txt')

#print('rename: ', rnm)

print('......................../////')

# re

char = 'this is checking.'
print(char)

cm = re.compile('is')
fd = cm.finditer(char)
print('compile: ', fd)

cnt = 0
for c in fd:
    cnt += 1
    print(c.group(), cnt)
    
    
#

def ser(n=None):
    try:
        with open(n) as op:
            rd = op.read()
            print(rd)

            ck = re.compile('hey!')
            wrd = ck.finditer(rd)
            print(wrd)

            for w in wrd:
                print(w.group())

    except:
        print('check the given serach pattern.')

    else:
        print('re pattern executed.')

    finally:
        print('re module.')
        
ser(dsk_pat)

print('........................//...........//')

from PIL import Image

img_path = 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\rename.jpg'
print('image paht: ', img_path)


#im = Image.open(img_path).show()
#im.save('e_rename.tga')

print('.................********..............')


imag_path = 'C:\\Users\\Gurramkonda\\OneDrive\\Desktop\\os_pract\\tataz\\'
print('images:', imag_path)

_j = '.jpg'

_p = '.png'

'''
path_ext = os.path.isdir(imag_path)
print(path_ext)
    
list_imag = os.listdir(imag_path)
print('list images: ',list_imag)

for j in list_imag:
    #print(j)
    if j.endswith('.png'):
        rm_ext = re.split('.png', j)
        #print(rm_ext[0])

        png_ext = os.path.join(rm_ext[0] + _j)
        print(png_ext)

        im = Image.open(imag_path + j)
        #im.show()

        im.save(imag_path + png_ext)

    else:
        if j.endswith('.jpg'):

            rm_ext = re.split('.jpg', j)
            #print(rm_ext[0])

            png_ext = os.path.join(rm_ext[0] + _p)
            print(png_ext)

            im = Image.open(imag_path + j)
            #im.show()

            im.save(imag_path + png_ext) '''

print('................************...............')

a = [[2,3]]*2
print(a)
print(':-', len(a))

print(a[1][0])
print(a[0][0])

a[0][0] = 4

print(a[0][0])
print(a)


aa = [1,2,3,4,5]
print(aa)
print(*aa)
print(aa.pop(0))
print(aa.pop(2))

ab = [[2,3],[2,3]]
print(ab)


ab[1][0] = 4
print(ab)
print(*ab)

print('.............****.......')


class TestA:
    def __init__(self):
        self.a = 'name'
        self.b = 'address'

    def items(self):
        self.val = (22,54,8)

    def prnt(self):
        
        print(self.a)
        print(self.b)
        print(self.val)

        

t = TestA()
t.items()
t.prnt()
    










    
