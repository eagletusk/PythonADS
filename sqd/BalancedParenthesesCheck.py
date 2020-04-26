# def balance_check(s):
#   # pairs = {')': '(','}':'{',']':'['}
#   stack = []

#   # if len(s)%2 !=0:
#   #   return False

#   # open_set = set('({[')

#   # matches = set([('(',')'),("{","}"),('[',']')])

#   # for paren in s:
#   #   print(stack)
#   #   if paren in open_set:
#   #     stack.append(paren)
#   #   else:
#   #     if len(stack) == 0:
#   #       return False
      
#   #     last_open = stack.pop()

#   #     if (last_open, paren) not in matches:
#   #       return False

#   return len(stack) ==0

def balance_check(s):
  stack = []

  if len(s)%2 != 0:
    return False

  open_set = set('({[')
 
  matches = set([('{','}'),("[","]"),("(",")")])

  for paren in s:
    # print(stack)
    if paren in open_set:
      stack.append(paren)
    else:
      if len(stack)==0:
        return False

      last_open = stack.pop()

      if (last_open, paren) not in matches:
        return False


  return len(stack) == 0
  


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print ('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)