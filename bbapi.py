import serial
import serial.tools.list_ports
import pygame.joystick

def serialScanPort():
    port_name = []
    port_list = list(serial.tools.list_ports.comports())
    for i in range(len(port_list)):
        port_name.append(port_list[i][0])
    return port_name

def serialPortSelect(serialclass, portname):
    serialclass.port = portname

def serialBaudRateSetting(serialclass, baudrate):
    serialclass.baudrate = int(baudrate)

def serialByteSizeSetting(serialclass, bytesize):
    BYTESIZEDICT = {'5':serial.FIVEBITS, '6':serial.SIXBITS,
                    '7':serial.SEVENBITS,'8':serial.EIGHTBITS}
    serialclass.bytesize = BYTESIZEDICT[bytesize]
    #serialclass.bytesize = int(bytesize)

def serialCheckoutBitSetting(serialclass, checkoutbit):
    CHECKOUTBITDICT = {'None':serial.PARITY_NONE, 'Even':serial.PARITY_EVEN,
                       'Odd':serial.PARITY_ODD, 'Mark':serial.PARITY_MARK,
                       'Space':serial.PARITY_SPACE}
    serialclass.parity = CHECKOUTBITDICT[checkoutbit]

def serialStopBitsSetting(serialclass, stopbits):
    STOPBITSDICT = {'1':serial.STOPBITS_ONE, '1.5':serial.STOPBITS_ONE_POINT_FIVE,
                    '2':serial.STOPBITS_TWO}
    serialclass.stopbits = STOPBITSDICT[stopbits]

def serialFlowControlSetting(serialclass, flowcontrolpar):
    if flowcontrolpar == r'RTS/CTS':
        serialclass.rtscts = True
        serialclass.xonxoff = False
    elif flowcontrolpar == r'XON/OFF':
        serialclass.rtscts = False
        serialclass.xonxoff = True
    elif flowcontrolpar == 'None':
        serialclass.rtscts = False
        serialclass.xonxoff = False