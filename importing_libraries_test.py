
import math as meth #renames the library for using inside ur code

'''
^safest bet, you can access anything in the module as long as you say "math." before it
It's also very clear and avoids confusion
'''


#from math import * 
'''
^asterisk imports the entire module, and you don't have to use math. before anything
but it's less clear and could be confusing
'''


#can rename the functions from the module as I showed below.
#from math import sqrt as takesqrt, exp as exponent #separate by comma to import multiple things
'''
^if you only want to import only a select few functions or things from a module, then you can do from ___ import ____
however, you won't have access to any math functions that you don't list (such as factorial)
'''

def main():
    nums = [1,2,3,4,5]
    x=3
    print(meth.sqrt(x))
    print(meth.exp(4))
    print(meth.factorial(x))#you need to import math, not just import sqrt and exp to use this
    #





if __name__ == "__main__":
    main()