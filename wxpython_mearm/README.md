# wxPython + PCA9685 + meArm
This is a demo of controlling meArm with wxPython GUI, 
where PCA9685 is a I2C control board for servo.


----------------------------------------------------------------------------------------------

Please finish the i2c config and install the wx python library, 
and you may find the detail at the [basic setup](../README.md).


## I2C config

Install i2c-tools.

```sh
sudo apt-get install -y python-smbus i2c-tools
```
Load i2c modules automatically after boot.

```sh
#/etc/modules
i2c-dev
i2c-bcm2708
```
Raspi-config -> Advanced Options -> I2C -> Enable automatically load I2C module.

```sh
sudo raspi-config
```
Reboot and test wether I2C is working.


```sh
sudo i2cdetect -l
```


## Install wxPython

```sh
sudo apt-get install -y python-wxgtk2.8
```

----------------------------------------------------------------------------------------------

## Let's try the mearm robotic arm with wxpython.

Clone this repository.

```sh
git clone https://github.com/YuanYouYuan/rpi-robotic-arm
```


Launch the program.

```sh
python rpi-robotic-arm/wxpython_mearm/main.py 
```


