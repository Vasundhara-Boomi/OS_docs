import os

def communication(child_writes):
	r, w = os.pipe()
	
	processid = os.fork()
	if processid:
		os.close(w)
		r = os.fdopen(r)
		print ("Parent reading")
		str = r.read()
		print( "Parent reads =", str)
	else:
		
		os.close(r)
		w = os.fdopen(w, 'w')
		print ("Child writing")
		w.write(child_writes)
		print("Child writes = ",child_writes)
		w.close()

child_writes = "Hello Everyone"
communication(child_writes)
"""
print("Parent reading")
print("Child writing")
print("Child writes =  Hello Everyone")
print("Parent reads = Hello Everyone")"""
