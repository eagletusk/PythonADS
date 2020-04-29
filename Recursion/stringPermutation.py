def permute1(s):
    output = []

    if len(s) ==1:
      output=[s]


    for i, let, in enumerate(s):
      print(i,let)
      print(s[:i]+s[i+1:])
      for perm in permute1(s[:i]+s[i+1:]):
        output += [let+perm]
        print(output)
    return output

    

# def permute(s):
#     out = []
    
#     # Base Case
#     if len(s) == 1:
#         out = [s]
        
#     else:
#         # For every letter in string
#         print(list(enumerate(s)))
#         for i, let in enumerate(s):
#             print(i,let)
#             # For every permutation resulting from Step 2 and 3 described above
#             for perm in permute(s[:i] + s[i+1:]):
                
#                 # Add it to output
#                 out += [let + perm]
#                 print(out)
#     return out

permute1('abc')
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# """
# RUN THIS CELL TO TEST YOUR SOLUTION.
# """

# from nose.tools import assert_equal

# class TestPerm(object):
    
#     def test(self,solution):
        
#         assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
#         assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
#         print ('All test cases passed.')
        


# # Run Tests
# t = TestPerm()
# t.test(permute)

