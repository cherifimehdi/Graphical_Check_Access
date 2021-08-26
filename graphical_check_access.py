from flask import Flask, render_template
from genie.testbed import load
import shutil
from diagrams.generic.os import Ubuntu
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

def Check_Access(testbed):

   #Save the decision for further use
   Device_Decision={}

   #Try access to each device
   for device in testbed.devices:
      try:
         testbed.devices[device].connect(log_stdout=False)
         Device_Decision[str(device)]="Access Ok"
      except Exception as e:
         Device_Decision[str(device)]="No Access"
   #Topology Devices Access
   Topology_Devices=[]

   with Diagram("Topology Access Result", show=False, filename="Topology_Result"):
      PC = Ubuntu("Admin")
      with Cluster("Network Entreprise"):

         SWITCH=Custom("Switch", "./static/Switch.png")
         for k,l in Device_Decision.items():
            Dev=Custom(k+'\n'+ l, "./static/"+testbed.devices[k].type+".jpg")
            Topology_Devices.append(Dev)
         PC >> SWITCH >> Topology_Devices
   shutil.move("Topology_Result.png", "static/Topology_Result.png")
   return Device_Decision

# Flask Part
app = Flask(__name__)
@app.route('/')

def result():
   testbed=load('connex.yml')
   return render_template('index.html', result = Check_Access(testbed))

if __name__ == '__main__':
   app.run(debug=True)
