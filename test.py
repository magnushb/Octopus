import serial

with serial.Serial('COM5') as ser:
    ser.baudrate = 19200
    ser.bytesize = 8
    ser.parity = 'N'
    ser.xonxoff = 1
    ser.rtscts = 1
    ser.timeout = 5
    print(ser.is_open)
    # Ask for current position
    ser.write(b'0PA?'+b'\r\n')
    answ = ser.readline()
    print('Current position: ',answ)
     # Ask for home
    ser.write(b'0OR?'+b'\r\n')
    answ = ser.readline()
    print('Home position: ',answ)
    # Move to absolute position
    ser.write(b'0PA20000'+b'\r\n')
    answ = ser.readline()
    print('Current position: ',answ)
    # Relative movement
    #ser.write(b'0PR50'+b'\r\n')
    #answ = ser.readline()
    #print('Home position: ',answ)
    # Ask for current position
    ser.write(b'0PA?'+b'\r\n')
    answ = ser.readline()
    print('Current position: ',answ)
     # Home
    #ser.write(b'0OR'+b'\r\n')
    #answ = ser.readline()
    #print('Current position: ',answ)
    # Define home
    #ser.write(b'0DH'+b'\r\n')
    #answ = ser.readline()
    #print('Current position: ',answ)
    # Ask for current position
    ser.write(b'0PA?'+b'\r\n')
    answ = ser.readline()
    print('Current position: ',answ)
    # Ask for acceleration
    ser.write(b'0AC?'+b'\r\n')
    answ = ser.readline()
    print('Current acceleration: ',answ)
    # Set acceleration
    ser.write(b'0AC500'+b'\r\n')
    answ = ser.readline()
    print('Set acceleration: ',answ)
    # Ask for acceleration
    ser.write(b'0AC?'+b'\r\n')
    answ = ser.readline()
    print('Current acceleration: ',answ)
