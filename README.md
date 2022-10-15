
<h1 align="center">
  <br>
  <a href="https://github.com/johabeere/SmartBoardBot"><img src="https://raw.githubusercontent.com/johabeere/SmartBoardBot/master/webserver/favicon.ico.png" alt="SmartBoardBot" width="200"></a>
  <br>
  Smart Board Bot
  <br>
</h1>

<h4 align="center">Raspberry Pi based Whiteboard Digitizer</h4>

<p align="center">
 
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/johabeere/SmartBoardBot/master/docs/img/Demo.gif)

## Key Features

* Interactive http Interface to control the board
* complete 2 axis motion system for large vertical surfaces
* Automatic Plotting of vector- and pixel-based images with inbuild scaling and positioning!
* scanning of the entire surface area to be implemented soon
* ...
* and build entirely on open source!

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](python.org) (which comes with [pip](https://docs.python.org/3/installing/index.html)) installed on your computer. From your command line:

```bash
#This software is configured to run on a Raspberry Pi. other platforms will need adjustments not included in these instructions.
# 0. Prerequisites:
      $ sudo apt-get update
      $ sudo apt-get upgrade
      $ sudo apt-get sqlite python3 python3-pip sqlite3 apache2 libapache2-mod-wsgi-py3 python3-setuptools python3-dev build-essential libsm6 libxext6 libgl1-mesa-glx libgeos++
      $ sudo pip3 install django==4.0.1 numpy pyserial django-mathfilters svg_to_gcode opencv-python pyyaml matplotlib shapley svgwrite scikit-image
# 1. Clone this repository
$ git clone https://github.com/johabeere/SmartBoardBot

# 2. Go into the repository
$ cd SmartBoardBot

# 3. Run the install script
$ sudo ./install.sh

# 4. Run the App
$ ./start.sh
# OPTIONAL: add autostart
#3. Run the install script with autostart
$ ./install.sh --autostart

```


## Download
In your working directory with ```git``` installed, execute ```git clone https://github.com/SmartBoardBot/```

## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [django](https://www.djangoproject.com/)
- [Marlin](https://github.com/MarlinFirmware/Marlin)
- [hatched](https://github.com/plottertools/hatched)
- [svg2gcode](https://github.com/vishpat/svg2gcode)
  
Thanks to all of them for their awesome work!

The following People contributed to this Project:

<span style="text-decoration:underline">From Germany:</span>
- Benedikt Döring
- Magdalena Geist
- Markus Hartenfels
- Yannick Nockmann
- Johannes Schraml
- Benedikt Zinn
  
<span style="text-decoration:underline">From the USA:</span>
- Lennard Kemper
- Lara Molitor
- Karla Nighbert

## Related
This project won the following awards:

- [VisionIng21](https://www.fking.de/ueber-vision-ing21) Wettbewerb 2022, First Prize
- KU [Jugend-Digitalisierungspreis](https://www.ku.de/digitalisierungspreis) 2022, 5th Prize

And was graciously funded by the following organizations:

- [Rotary Club Höchstadt](https://www.facebook.com/RotaryClubHoechstadt/)
- [MintEC Network](https://www.mint-ec.de/) 
- [Dr. Gerda Stetter Foundation](https://www.itq.de/en/itq-group/gerda-stetter-foundation/)
- [Gymnasium Höchstadt a. d. Aisch](https://gymnasium-hoechstadt.de/)

## License

Fell free to use any part of this project that seems usefull to you, as long as you respect the licenses for the other integrated projects and attribute this github page.

---

> GitHub [@johabeere](https://github.com/johabeere) &nbsp;&middot;&nbsp;
> Twitter [@joha_beere](https://twitter.com/joha_beere)

