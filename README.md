# Hackpad.v1

This is a 9 key macropad based on XIAO-RP2040 microcontroller, it features 2 leds and 9 keys which can custom mapped to whatever you require it for by changing the mapping in the firmware.py file.
Purpose of this macorpad is to allow easy and quick access to important functions according to your needs such as a single key be assigned to undo or redo, pause or play any media or whatever key combination/key you wish to set it to .A working schematic below shows how this project works:

<img width="1004" height="676" alt="image" src="https://github.com/user-attachments/assets/a76cfcdd-473a-4473-b649-e061c252ab18" />

The Digital pins of the Xiao board are connected to mechanical switches and 2 leds. The board provides power to the leds and receives input from the keys which is then transmitted into keystrokes via the kmk firmware, and thus show designated output on your screen !

The whole design is made on a 2-layer PCB board as shown below:

<img width="560" height="701" alt="image" src="https://github.com/user-attachments/assets/e9c5d2df-f9c5-4f96-b074-3443540b065d" />



A 3D model view of the PCB:

<Front> <img width="469" height="529" alt="image" src="https://github.com/user-attachments/assets/e5c20f5a-7a61-4b02-a311-0e5e28bffac1" />
<Back>  <img width="573" height="562" alt="image" src="https://github.com/user-attachments/assets/9f0ec0f1-a409-4f18-a37f-503707be6563" />

I have also designed a case for this to complete the macropad with slots for the 9 keys:

<View of the 3d model>

<bottom> <img width="785" height="721" alt="image" src="https://github.com/user-attachments/assets/c4218b55-5f12-4638-92c2-ce31ab89f992" />

<top> <img width="667" height="672" alt="image" src="https://github.com/user-attachments/assets/01473483-e1e6-4564-8ab2-32d3f8c1e7c4" />

This project was made using Kicad,Onshape and python for the firmware, the kmk library was used for mapping the keys and providing the output.



