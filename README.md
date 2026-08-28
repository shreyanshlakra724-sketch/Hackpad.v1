# Hackpad.v1

A macropad with 9 keys and two leds, made using Kicad,Onshape and kmk for firmware part, you can easily set the keys to what you want by changing them in the firmware.py file.

Made it over a span of 5 days, had to remake the case agian due to wrong measurments.
Some images of the parts:

<img width="377" height="434" alt="image" src="https://github.com/user-attachments/assets/6d2434d4-45cd-4979-9c79-10f01b072ca6" />
PCB-3d view

<img width="793" height="586" alt="image" src="https://github.com/user-attachments/assets/5edaa88d-45aa-4730-b325-8b2d450b5fe9" />
<img width="792" height="639" alt="image" src="https://github.com/user-attachments/assets/0e586621-00ac-4612-8a6e-97ca45d05913" />

Upper and lower case

"Reference","Qty","Value","DNP","Exclude from BOM","Exclude from Board","Exclude from Simulation","Exclude from Position Files","Footprint","Datasheet"
"D1,D2","2","SK6812MINI","","","","","${EXCLUDE_FROM_POS_FILES}","LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm","https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf"
"SW1,SW2,SW3,SW4,SW5,SW6,SW7,SW8,SW9","9","SW_Push","","","","","${EXCLUDE_FROM_POS_FILES}","Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB",""
"U1","1","XIAO-RP2040-SMD","","","","","${EXCLUDE_FROM_POS_FILES}","Seed_XIAO:XIAO-RP2040-DIP",""
