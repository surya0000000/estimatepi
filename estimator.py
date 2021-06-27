import random

def estimatewallis(iters=1000):
 acc=1.0
 for n in range(1, iters+1):
  acc=acc*(4*(n**2))/(4*(n**2)-1)
 acc=2*acc
 return acc
 #ender_template("pi.html",alg="Wallis Algorithm",total=iters,ans=acc)
  
  
  
 
def estimatemc(total=15000):
 inside=0.0
 for i in range(total):
  x=random.random()
  y=random.random()
  if(x**2+y**2)<=1:
   inside+=1.0
 return 4*inside/total
 #render_template("pi.html",alg="MonteCarlo Simulation",total=total,ans=4*inside/total)
