x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x) 

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 