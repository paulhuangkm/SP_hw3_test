import os
for i in range(20):
    a = input()
    a = a + " > {}.out &".format(i)
    os.system(a)
