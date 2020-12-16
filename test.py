import serial

with serial.Serial('/dev/ttyr02') as ser:
    ser.baudrate = 19200
    ser.bytesize = 8
    ser.parity = 'N'
    ser.xonxoff = 1
    ser.rtscts = 1
    print(ser.is_open)