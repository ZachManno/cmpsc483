
g = AVG(x,y,z)
ANS= AVG(g,b,p)

"g = x+y+z/3" , **AVG**
"(((x+y+z)/3),b,p)/3 " **AVG**


AVG(3,4,5)

(3+4+5/3 , **AVG**)

AVG((4*4),(5*5),(6/3))

(4*4)+(5*5)+(6/3) / 3 , AVG(x,y,z), AVG(g,b,p)




x=5
y=7
AVG(x,y,z)
AVG(x,y,z) ,

"x+y+z/3" , "**x=5**" , "**y=7**"

"main equation" "&& **AVG** ** x=5**  x number of flags, begins and ends with &&" "secondary equation"


ANS = 5+7
"5 + 7"

ANS = x + 5
"x + 5"

ANS = x + y
"x + y"

x=5
ANS = x+y
"x+y" "&& **x=5** &&"


x=5
y=7
ANS = x+y
"x+y" "&& **x=5** **y=7** &&"

x=5
y=7
ANS = AVG(x,y,z)
"x+y+z/3" "&& **x=5** **y=7** &&"

x=5
y=7
z=x+y
ANS = AVG(x,y,z)
"x+y+(x+y)/3" "&& **x=5** **y=7** **AVG** &&" "z = x+y"


ALGORITHM:

1. scan through variable declarations, store
2. Scan through equations that do not begin with "ANS"
     -parse out any keywords (ie AVG)
     -store all information
3. Scan equation that begins with ANS
    - scan each variable in ANS equation, subsitute with other equations as necessary, add flags
4. Return final ANS equation and flags
5. Return all other equations and flags









































12+z/3


AVG(L3)

def AVG_func(l1):
    length = len(l1)
    print(length)

AVG_func(l1)