AVG()

algorithm:
#"preprocessing" just means we need to turn input into pure algebraic expression before formally parsing
breakdown(){

    #convert the input code into an eqn representing it
    #important flag keywords: AVG, SQRT, SQR, SDEV, VAR, etc.
    #return the main eqn as a string, then the flags as one string, then the sub eqns
}


"""
['SQUARE', [['AVG', [['5'], ['7']]], 'AREA', ['x', 'y+4']]]

['SQUARE', [[ 'AVG', ['5', '7'] ], 'AREA', ['x', 'y+4']]]

['SQUARE', [ (5+7)/2 , 'AREA', ['x', 'y+4'] ]       ]

['SQUARE', [ (5+7)/2 , (x)*(y+4) ]       ]

[(5+7)/2 * (x)*(y+4)  ]



['SQUARE', [   ['AVG', [['5'], ['7']]], 'AREA', ['x', 'y+4']   ]       ]

['SQUARE', [   [ 'AVG', ['5', '7']   ], 'AREA', ['x', 'y+4']   ]       ]

['SQUARE', [   [ (5+7)/2 ], 'AREA', ['x', 'y+4']   ]       ]

['SQUARE', [   [ (5+7)/2 ], 'AREA', ['x', 'y+4']   ]       ]

['SQUARE', [   [(5+7)/2  ] , 'AREA', ['x', 'y+4']   ]       ]

['SQUARE', [    [(5+7)/2 ], (x)*(y+4)   ]       ]

['SQUARE', [    (5+7)/2 , (x)*(y+4)   ]       ]

[ ((5+7)/2) * ((x)*(y+4)) ]



[    'x+AVG', ['x', 'y+5', 'z'], '*SQUARE', ['x+y', 'z*f']    ]

[    'x+(x+(y+5)+z/3', '*SQUARE', ['x+y', 'z*f']    ]

[    'x+(x+(y+5)+z/3', '*(x+y) * (z*f)'    ]

if len(list) > 1, concatenate




['p*AVG', ['x', 'AREA', ['y', 'z'], 'AVG', ['a', 'b', 'c']], ' + j']

['p*AVG', ['x', '(y)*(z)', 'AVG', ['a', 'b', 'c']], ' + j']

['p*AVG', ['x', '(y)*(z)', '(a+b+c)/3'], ' + j']

['p*(x+(y)*(z) + ((a+b+c)/3) )/3', ' + j']


Start left to right
When FLAG is hit, the next index will be a list of the arguments to the flag
keep recursing through this
each arg to the flag might contain additional flags
recurse through these
once all flags in the args to the flag are parsed out, and END OF ARG LIST IS REACHED:
        REPLACE the flag with the parsed version using the macro function w arg list as a parameter
        DELETE the args list from the original list
Continue through list

***FLAGS can only be to the RIGHT of a list item. IE 'p*AVG' is possible, but 'AVG * p' is not

^^^ A list that has only one element with no flags needs to delete the list part ie [x+y/3] -> x+y/3

This example:
given:
['p*AVG', ['x', 'AREA', ['y', 'z'], 'AVG', ['a', 'b', 'c']], ' + j']
AVG is found, next is going to be list of args for AVG = ['x', 'AREA', ['y', 'z'], 'AVG', ['a', 'b', 'c']]


(I skipped area on accident, forget this)
['p*AVG', ['x', '(y)*(z)', 'AVG', ['a', 'b', 'c']], ' + j']
AVG is found in list of args to AVG, next is gonna be list of args to this NEW AVG = ['a', 'b', 'c']
Go through EACH ONE, NO FLAGS, END OF LIST IS REACHED, CALL MACRO
macro_avg([a,b,c]) returns "a+b+c/3"


['p*AVG', ['x', '(y)*(z)', '(a+b+c)/3'], ' + j']
replace 'AVG' with (a+b+c)/3

keep on scrolling through original AVG. END IS REACHED (the '+ j' is not associated with the AVG at all)
call macro with these three long arguments
replace 'AVG' with the result of the macro function
['p*(x+(y)*(z) + ((a+b+c)/3) )/3', ' + j']

everything is macro'd out. now just append the strings


['SQUARE', [['AVG', [['5'], ['7']]], 'AREA', ['x', 'y+4']]]

['SQUARE', [ ['AVG', ['5', '7']], 'AREA', ['x', 'y+4'] ]      ]

['SQUARE', [ '5+7/2', 'x*(y+4)' ]      ]

['5+7/2 * x*(y+4)'     ]










""""