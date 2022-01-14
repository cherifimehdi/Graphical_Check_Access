Auto web-based graphical check access to network devices
=====================================
Exploiting Genie/pyATS, Flask, APScheduler and Diagrams to Validate/Monitor access to network devices

This use case aims to generates automatically the topology of the entreprise showing if there is an access to the network devices. It leverages the modules [Flask](https://flask.palletsprojects.com/en/2.0.x/), [APScheduler](https://apscheduler.readthedocs.io/en/3.x/) and [Diagrams](https://diagrams.mingrammer.com/) with [Genie/pyATS](https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/index.html) framework.

In summary, this project : 
- The function __Check_Access__ is scheduled in background with __APScheduler__ and excecuted periodically in order to retrieve the actual topology access state of the devices.

- A Flask route that retrieve and display the topology access state with legend indicating the access state according to the color : <span style="color:red">Red device</span> in case ___No Access___ and <span style="color:blue">Blue device</span> in case ___Access Ok___. There is two templates: __Auto Access State__ and __On demand Access State__. In both cases, there is a GIF animation indicating that the topology access state is on process in the case that this latter is not previusly generated or deleted in some reason by the admin.
1. __Auto Access__ : Retrieve periodically the topology access state with auto refreshing the web page. Feel free to change the period time in __index_auto_refresh_state.html__
2. __On-demand Access__ : The admin can retrieve the actual topology access state of the devices using a botton. 


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
