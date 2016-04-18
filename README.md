# This is a note for rpi-robotic-arm@cavedu 

## Setup

### OS: using Raspbian

### I2C config

Install i2c-tools.

```shell
sudo apt-get install -y python-smbus i2c-tools
```
Load i2c modules automatically after boot.

```shell
#/etc/modules
i2c-dev
i2c-bcm2708
```
Raspi-config -> Advanced Options -> I2C -> Enable automatically load I2C module.

```shell
sudo raspi-config
```
Reboot and test wether I2C is working.

```shell
sudo i2cdetect -l
```

### Setup vnc (optional)

Install vnc server and start it with port 5901 (:1), display resolution 1920x1080 (-geometry), pixel depths 16 (-depth).

```shell
sudo apt-get -y install tightcvcserver
vncserver :1 -geometry 1920x1080 -depth 16
```

Launch vncserver at startup, create a script, change its mod to 755, and then add it to startup process.

Create a script /etc/init.d/tightvncserver.

```shell
#!/bin/bash
export USER='pi'
eval cd ~$USER

case "$1" in
  start)
    su $USER -c '/usr/bin/vncserver :1 -geometry 1920x1080' 
    echo "Starting vncserver for $USER"
    ;;
  stop)
    pkill Xtightvnc
    echo "vncserver stopped"
    ;;
  *)
    echo "Usage: /etc/init.d/tightvncserver {start|stop}"
    exit 1
    ;;
esac
exit 0
```
Change mode and add it to startup process. Remember reboot for work.

```shell
sudo chmod 755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults
```

Monitor ports of vncserver.

```shell
netstat -nutlp
```

Log in on client and config the environment variable $DISPLAY to vncviewer (under ssh login).

```shell
vncviewer <ip address of rpi>:5901
export DISPLAY=":1" 
```














