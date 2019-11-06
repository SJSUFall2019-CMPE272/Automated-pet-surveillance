## Project Proposal #1

# Automated Pet Surveillance

Atharva Munshi        
Kapil Mulchandani  	    
Namrata Deshmukh           
Vijay Ghanshani

A software application that keeps track of the pet’s activities and reports anomalous behavior of the pet to owner via mobile app. 

# Abstract:
The increase in the computational power of computers has made it possible to capture important information, make use of the context and interact directly with the physical object. The IoT provides a set of standards and methodologies to associate an object in the real world. In our project, the proposed device will help the dog owners to keep an activity track on their pet remotely via webcam and feed them by just clicking a button or setting regular intervals for food dispense. It will also send the notifications to the owner whenever the dog behaves abnormally like excessive barking and thus fulfilling the need of the customers by letting owners leave their pets at home without any worries and let them take care of their pet's food requirements while they are not home.

# Architecture Diagram:
![Untitled Document](https://user-images.githubusercontent.com/33183783/66629690-648cc380-ebb7-11e9-8a2f-4f85bad2a419.png)
Technology stack: 

•	Software Technologies: Android Studio, Java, Python, Raspbian OS, Kotlin, SQL database, AWS EC2

•	Hardware Technologies: Raspberry Pi, Webcam, Servomotor SG90, MCP3008 ADC, Sound Sensor, Jumper Cables.

Raspberry Pi : It will act as the heart of the system with all the components mounted on it for synchronization and processing.

MCP3008 ADC : This will convert the analog sound signals to digital signals which will be required as input to Raspberry pi. As soon as the raspberry pi detects the digital signal in form of voltage, it will call the API designed to send the push notification to the pet owner. 

BreadBoard : This will be used to connect Electret Microphone Amplifier - MAX4466 (sound sensor) with Raspberry Pi.

SG90 Servo Motor : This will be used to dispatch the food for the pet and will be controlled by centralized Raspberry Pi.

## Empathy mapping
### User : Paula
  (A web developer and pet owner who works part time at client location.)
![Empathy mapping](https://user-images.githubusercontent.com/31982121/68059193-c1603300-fcb8-11e9-9837-e5f06fd8c285.jpg)

## Hill Statements:
Hill statement is used to describe a specific functionality user is trying to achieve by answering 3 main questions: Who, What and How.
### Project hill statement:
A pet owner using an automated surveillance system will be able to monitor the pet present in the range of cameras and feed them without being present at the same location as the pet.

An owner will be able alerted by the system in case of any unusual behavior expressed by his/her pet eliminating the need of constant monitoring through cameras.

