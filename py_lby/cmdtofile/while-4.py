x = ''
while x !='q':
    print 'hello'
    x = raw_input("please input something q for quit:")
    if not x:
        break
    if x =='C' :
        continue
    print 'hello one more time'
    
else:
    print 'end.'



##>>> ================================ RESTART ================================
##>>> 
##hello
##please input something q for quit:hello
##hello one more time
##hello
##please input something q for quit:c
##hello one more time
##hello
##please input something q for quit:C
##hello
##please input something q for quit:k
##hello one more time
##hello
##please input something q for quit:C
##hello
##please input something q for quit:
##>>> ================================ RESTART ================================
##>>> 
##hello
##please input something q for quit:q
##hello one more time
##end.
##>>> ================================ RESTART ================================
##>>> 
##hello
##please input something q for quit:0
##hello one more time
##hello
##please input something q for quit:q
##hello one more time
##end.
##>>> 
