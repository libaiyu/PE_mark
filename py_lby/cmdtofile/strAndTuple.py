>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> Zo in name
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Zo in name
NameError: name 'Zo' is not defined
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
	print('***' + i + '***')

	
***Z***
***o***
***p***
***h***
***i***
***e***

>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
>>> eggs = [1,2,3]
>>> eggs = [4,5,6]
>>> eggs
[4, 5, 6]
>>> eggs = [1,2,3]
>>> del eggs[2]
>>> eggs
[1, 2]
>>> del eggs[0]
>>> eggs
[2]
>>> del eggs[0]
>>> eggs
[]
>>> eggs.append(5)
>>> eggs.append(4)
>>> eggs.append(6)
>>> eggs
[5, 4, 6]
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3
>>> eggs[1]=99
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    eggs[1]=99
TypeError: 'tuple' object does not support item assignment
>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>
>>> tuple(['cat','dog',5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']

>>> spam = 42
>>> cheese =  spam
>>> spam
42
>>> spam = 100
>>> spam
100
>>> cheese
42
>>> spam = [0,1,2,3,4,5]
>>> cheese =  spam
>>> cheese[1] = 'hello'
>>> spam
[0, 'hello', 2, 3, 4, 5]
>>> cheese
[0, 'hello', 2, 3, 4, 5]




