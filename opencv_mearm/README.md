# This is a demo for visual recognition on pi.

## Preparation

Install opencv(python)

```shell
sudo apt-get install -y libopencv-lib python-opencv
```

## Usage

Clone this repository.

```sh
git clone https://github.com/YuanYouYuan/rpi-robotic-arm
```
Change work directory to here.

```sh
cd rpi-robotic-arm/opencv_mearm
```

Run mask_contour_test to recognize your object.

```shell
python mask_contour_test.py
```
Run wx_mearm to manipulate robotic arm with GUI.

```shell
python wx_mearm.py
```

Run opencv_mearm to track an object and grip it automatically.

```shell
python opencv_mearm.py
```


