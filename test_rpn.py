import rpn
import math 

def test_rpn():
    # happy path cases
    assert(rpn.evaluate('3 2 +') == 5)
    assert(rpn.evaluate('7 3 -') == 4)
    assert(rpn.evaluate('2 5 *') == 10)
    assert(rpn.evaluate('10 2 /') == 5)
    assert(rpn.evaluate('2 4 6 * +') == 26)
    assert(rpn.evaluate('2 6 - 5 +') == 1)
   
    # edge cases
    assert(rpn.evaluate('2') == 2)
    assert(rpn.evaluate('3.5') == 3.5)
    assert(rpn.evaluate('-7') == -7)
    assert(rpn.evaluate('25') == 25)
    
    #math.isclose()
    assert(math.isclose(rpn.evaluate('1 3 /'), 1/3))