def func():
  return 1

s = 'hello world'

def check_for_globals():
  # print(locals())
  # print(globals().keys())
  pass

check_for_globals()

def hello(name="John"):
  return "hello " + name

print(hello())

greet = hello
print(greet())

del hello
print(greet())

def other(func):
    print('Other code would go here')
    print(func())

other(greet)
other(func)

def decorator(func):
  def wrap_func():
    print('...Decoration...')
    func()
    print('....Decoration....')
  return wrap_func

# def func_needs_decorator():
#   print("this function needs some decoration")

# func_needs_decorator()

# func_needs_decorator = decorator(func_needs_decorator)
# func_needs_decorator()

@decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()