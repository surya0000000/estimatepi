from flask import Flask
import random
from flask import render_template,request
import estimator



app=Flask("Pi estimator")

@app.route("/")
def hello():
 return render_template("home.html")
 

@app.route("/estimate" ,methods=["POST"])

def estimate():
 algorithms=request.form['algorithm']
 iterations=request.form['iterations']
 if algorithms=="mc":
  estimate=estimator.estimatemc(int(iterations))
 elif algorithms=="wallis":
  estimate=estimator.estimatewallis(int(iterations)) 
 names={"mc":"MonteCarlo Simulation","wallis" : "Wallis product Estimation"}
 return render_template("pi.html",algorithm=names[algorithms],total=iterations,ans=estimate)
 
 

   

 
if __name__=="__main__":
 app.run()
 
  
