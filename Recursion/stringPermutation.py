def permute(s):
    
    pass


'''
permute('abc')
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

'''

"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""

from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print 'All test cases passed.'
        


# Run Tests
t = TestPerm()
t.test(permute)

