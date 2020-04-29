def reverse1(s):
    s1 = ''
    if len(s) == 0:
      return 1

    s1 = ''.join(s1+s[len(s)-1])
    s1 = ''.join(s1+s[0:len(s)-1:])
    print(s1)
    return s1 + reverse1(s1)


def reverse(s):
    if len(s) <=1:
      return s
    print(s)
    return reverse(s[1:]) +s[0]

    

    '''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print ('PASSED ALL TEST CASES!')
        
# Run Tests
test = TestReverse()
test.test_rev(reverse)

print(reverse('hello'))