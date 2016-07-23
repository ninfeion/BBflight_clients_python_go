ui convert to py

cmd
cd
pyuic5 -o codeFile.py -x yourUIfile.ui


qrc convert to py

cmd 
cd
pyrcc5 -o images.py images.qrc

32bytes:
client to flight
|7|6|5|4|3|2|1|0|
|       0xaa    | 00
|       0xaa    | 01
|       ad0     | 02
|       ad1     | 03
|       ad2     | 04
|       ad3     | 05
|       ad4     | 06
|   try connect | 21
|       roll    | 07
|       roll    | 08
|       roll    | 09
|       roll    | 10
|       pitch   | 11
|       pitch   | 12
|       pitch   | 13
|       pitch   | 14
|       yaw     | 15
|       yaw     | 16
|       yaw     | 17
|       yaw     | 18
|       thrust  | 19
|       thrust  | 20
|   resevered   | 22
|   resevered   | 23
|   resevered   | 24
|   resevered   | 25
|   resevered   | 26
|   resevered   | 27
|   resevered   | 28
|   resevered   | 29
|   0xff        | 30
|   0xff        | 31

AA AA 34 C3 10 10 11 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF

flight client
|7|6|5|4|3|2|1|0|
|       0xaa    | 00
|       0xaa    | 01
|       ad0     | 02
|       ad1     | 03
|       ad2     | 04
|       ad3     | 05
|       ad4     | 06
|       connect | 21 07
|       roll    | 07 08
|       roll    | 08 09
|       roll    | 09 10
|       roll    | 10 11
|       pitch   | 11 12
|       pitch   | 12 13
|       pitch   | 13 14
|       pitch   | 14 15
|       yaw     | 15 16
|       yaw     | 16 17
|       yaw     | 17 18
|       yaw     | 18 19
|       thrust  | 19 20
|       thrust  | 20 21
|   M1          | 22
|   M2          | 23
|   M3          | 24
|   M4          | 25
|   Battery     | 26
|   LinkQuality | 27
|   resevered   | 28
|   resevered   | 29
|   0xff        | 30
|   0xff        | 31

AA AA 34 C3 10 10 11 01 31 32 33 34 31 32 33 34 31 32 33 34 06 40 5a 5a 5a 5a 5a 5a 00 00 FF FF

Thread :
1. serial recieve
2. Ui serial recieve data handle
3. Ui joystick detect
4. Ui radio send