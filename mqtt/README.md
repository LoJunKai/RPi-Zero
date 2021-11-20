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

# Installation

``` bash
https://github.com/LoJunKai/RPi-Zero.git
pip3 install -r requirements.txt
```

# MOSQUITTO BROKER
 1. Install mosquitto from https://mosquitto.org/download/ on your computer
 2. Run the installer


# MQTT

After installing all the requirements

1. Connect the ports between the rpi and your computer, by running this code on your computer's cmd
`ssh -R 1883:localhost:1883 pi@raspberrypi.local`

2. Open another cmd and go to the folder with the downloaded binaries for mosquitto
   (for windows, it's C:\Program Files\mosquitto)
   and run the following command: mosquitto

3. Run the mqtt_client_sub.py code on your computer.

4. Run `mqtt_client_pub.py --times 100` on you rpi
   `100` can be changed, depending on how many times you want to publish the file.
