import time
import atexit
from flask import Flask, render_template
from genie.testbed import load
import shutil
from diagrams.generic.os import Ubuntu
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from pytz import timezone
import logging
from apscheduler.schedulers.background import BackgroundScheduler

testbed=load('connex.yml')

app = Flask(__name__)

@app.route('/')
# In case Auto Check Access
def result():
   return render_template('index_auto_refresh_state.html')

'''
# In case of On-Demand Check Access
def result():
   return render_template('index_on-demand_state.html')
'''

def Check_Access(testbed):

   #Save the decision for further use
   Device_Decision={}

   #Try access to each device
   for device in testbed.devices:
      try:
         testbed.devices[device].connect(log_stdout=False)
         Device_Decision[str(device)]=testbed.devices[device].type
         testbed.devices[device].disconnect()
      except Exception as e:
         Device_Decision[str(device)]=testbed.devices[device].type+'-no-access'
   #Topology Devices Access
   Topology_Devices=[]

   with Diagram("Topology Access Result", show=False, filename="Topology_Result"):
      PC = Ubuntu("Admin")
      with Cluster("Network Entreprise"):
         SWITCH=Custom("vSwitch", "./static/vSwitch.png")
         for k,l in Device_Decision.items():
            Dev=Custom(k+'\n'+ testbed.devices[k].connections.cli.protocol+":"+str(testbed.devices[k].connections.cli.port), "./static/"+l+".jpg")
            Topology_Devices.append(Dev)

         PC >> SWITCH >> Topology_Devices
   shutil.move("Topology_Result.png", "static/Topology_Result.png")

   return Device_Decision


# Configure the scheduling process of the Check_Access function
scheduler = BackgroundScheduler()
scheduler.add_job(func=Check_Access, trigger="interval", seconds=180, args=[testbed], timezone='Europe/London')
scheduler.start()

# Deactivate the logs in Flask server except the ERROR level
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__=='__main__':
   app.run()
