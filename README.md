# 50.012 Networks Project
## Team 10 - RPi-Zero
* Yee Yi Xian
* Lo Jun Kai
* Priscilla Pearly Tan Pei En
* Lau Yu Hui
* Tan Jing Heng Darryl

# Repository guide
* [gRPC](./grpc/README.md)
* [MQTT](/mqtt/README.md)
* [Hybrid Model](./hybrid/README.md)
* [Testing Scripts](./testing/)

# Set up Raspberry PI

1. Install [Raspberry Pi OS lite]((https://www.raspberrypi.com/documentation/computers/getting-started.html)) in RPi.
2. With the SD card connected, run the [RPi Imager](https://www.raspberrypi.com/software/).
3. Press `ctrl + shift + x` to open settings and fill in the options for wifi, ssh and password.
4. Transfer the SD card to RPi and connect the RPi to a power source.
5. Boot into the Raspberry Pi using SSH. Can either use `raspberrypi` or `raspberrypi.local` or look at your router entry to determine IP address of the RPi. Tutorials: [VSC](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/)
6. Install PIP

    ```bash
    sudo apt-get instal python3-pip
    ```

7. Install GIT

    ```bash
    sudo apt-get install git
    ```

## Installation

``` bash
https://github.com/LoJunKai/RPi-Zero.git
pip3 install -r requirements.txt
```
