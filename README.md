# GarageDoorStatus_BB_Flask
 
 
 Add this to cron
```
 @reboot sh /home/debian/launcher.sh >/home/debian/logs/cronlog 2>&1
 ```

 Add this to homeassistant configuration.yaml

 ```
sensor N
    - platform: rest
    name: GarageDoor
    resource: http://flask_web_server_ip:port/api_states
 ```
 replace N with the number you want to specify the sensor as
 replace flask_web_server_ip (and port) with the IP address (and port) of the beaglebone running flask web server
 