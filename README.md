# Sensor-Multitool
## Target
The Sensor-Multitool shall be a server or portable program for 
* 👨‍⚕ scientists
* 👨‍🏫 schools
* 👨‍💻 programming beginners. 

## Usage
You will be able to select a type of sensor and this program will give you instructions how to wire it to an Arduino. 
After that you can hook that Arduino to a PC and this program will program your Arduino for that specific sensor. 
Now the program shows you all the values the sensor can measure in many different types of charts or tables. 

## About
The program is a fork of [Klima-alarm](https://github.com/Jugendhackt/klima-alarm), 
which was a projekt from the _hackathon_ **"JugendHackt"**, where I worked one weekend with a couple of others to show the effects of greenhouse gases with a gas sensor. 

So the program as it is now is only able to this part and isn't really easy to init without any knowledge of **arduinos, raspberrys, node.js** and so on.
But for this I want to simplify the usage so that even teachers and student in high schools are able to use it. 

## Installation
First you have to clone this git to your local PC ( [[📥] master.zip](https://github.com/Geronymos/Sensor-Multitool/archive/master.zip) ). 

**You need to have npm and node.js installed!**

To download all dependencies just type this in the console after entering `./node-server/`
```shell
npm install 
```

To run the program type this in the same directory in the console
```shell
npm start 
```

## Preview
| Line chart 📈 | Pie chart 😋 |
| ---------- | --------- |
| ![Line chart picture](docs/Screenshot-2019-09-29-line-chart.png) | ![Pie chart picture](docs/Screenshot-2019-09-29-pie-chart.png) |