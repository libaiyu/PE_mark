x = ''
while x !='q':
    print 'hello'
    x = raw_input("please input something q for quit:")
    if not x:
        break
else:
    print 'end.'


##>>> ================================ RESTART ================================
##>>> 
##hello
##please input something q for quit:a
##hello
##please input something q for quit:b
##hello
##please input something q for quit:q
##end.
##>>> ================================ RESTART ================================
##>>> 
##hello
##please input something q for quit:a
##hello
##please input something q for quit:b
##hello
##please input something q for quit:
##>>> 
