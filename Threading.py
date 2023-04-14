import threading
import inspect
def print_cube(num):
    print("Cube: {}".format(num * num * num))

#cube(10)
t1 = threading.Thread(target=print_cube, args=(10,))
t1.start()
t1.join()

print(dir(threading.Thread))
print("\n")
print(inspect.signature(threading.Thread))
print("\n")
#print(help(threading.Thread))
print("\n")
print(dir(threading))











'''
#2 To display the arguments/signature of built-in classes only.
import inspect 
import threading
from threading import Thread, Barrier
print(dir(Thread))
print("\n")
print(inspect.signature(Thread))
print("\n")
print(inspect.signature(Barrier))
print("\n")
#print(inspect.signature(threading))
'''







'''
#1 Modules to import for threading (involves help docs, dir for classes and display methods in module)
import threading
from threading import *
#from threading import Barrier
from inspect import getmembers, isfunction

from threading import Thread
#print(getmembers(Thread, isfunction))
#print(Thread.methods)
#print(dir(Semaphore))
print("\n")

#print(dir(Thread))
print("\n")

#print(help(Thread))
#print(dir(threading))
for x in dir(Thread):
    print(x)
'''