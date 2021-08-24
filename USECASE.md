Auto web-based graphical check access to network devices
=====================================
Exploiting Genie/pyATS, Flask and Diagrams to Validate/Monitor access to network devices

This use case aims to generates automatically the topology of the entreprise showing if there is an access to the network devices. It leverages the modules [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Diagrams](https://diagrams.mingrammer.com/) with [Genie/pyATS](https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/index.html) framework.

In summary, this project : 
- Periodically attempt access to network devices

- Display the result as a topology with the result displayed below each device name : ___Access Ok___ or ___No Access___

# Important Remarks

1. Please run once the script graphical_check_access.py and please keep refresh priodically the web page of the project (http://127.0.0.1:5000 for this case).
The project generates for each refresh a new topology and then, a new state based on the access to the network devices. You can automate the refreshing process  by using either some extention such as [Tab Reloader](https://github.com/james-fray/tab-reloader/) or some python module such as [pyautogui](https://pyautogui.readthedocs.io/en/latest/) or [selenium](https://selenium-python.readthedocs.io/getting-started.html)  
It is imortant to indicate the part of the script __graphical_check_access.py__ that makes the update in topology for each refresh:

```python
return render_template('index.html', result = Check_Access(testbed))
```
   with __Check_Access(testbed)__ is the function that ensures the access check to the devices throught their management interfaces

2. The image __Topology_Result.png__ containing the result rendening in the web page is overwritten for each refreshing of the web page. The topology is the same as that used in this demo as multi access topology. You can generate a topology according to yours but the goal here is to check access then it is
better to simulate any physical topology as logical multi access topology to avoid modification in the script and to simplify the analyse of result.



## White Paper
Please refer to these white papers:

[Getting started with pyATS](https://developer.cisco.com/docs/pyats-getting-started/)

[Getting started with pyATS Library Genie : Kickoff your Genie experience!](https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/index.html)

[Welcome to Flask’s documentation](https://flask.palletsprojects.com/en/2.0.x/) 

[Diagrams - Diagram as Code](https://diagrams.mingrammer.com/)

Here a blog post from [Hank Preston](https://blogs.cisco.com/author/hankpreston) in case of using CML2: [How can I automate device configurations using CML2?](https://blogs.cisco.com/developer/363-askhankcml2-01)


## Related Sandbox

Cisco DevNet Sandbox [Cisco Modeling Labs](https://devnetsandbox.cisco.com/RM/Diagram/Index/45100600-b413-4471-b28e-b014eb824555?diagramType=Topology)

## Solutions on Ecosystem Exchange
How pyATS can be used as an end-to-end DevOps automation ecosystem: [Accelerating your DevOps with pyATS](https://developer.cisco.com/pyats/)