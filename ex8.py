'''formatter varaible .foramt is a function
passing arguments in that function once as integer 1,
one as "strings", once as bolean operators,
 once as the varaible itsself, once as four "strings" '''
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format (one, two, three, four))
print(formatter.format (True, False, False, True))
print(formatter.format (formatter, formatter, formatter, formatter ))
print(formatter.format (
    "There once was a man called Ted",
"Who loved giving young men head",
"He'd lay on his back as he licked a ball sack",
" and gag on that cock will he was dead")