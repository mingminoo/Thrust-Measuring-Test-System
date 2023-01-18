# This is a sample Python script.

# serial Communication class import
import serial
import serial.tools.list_ports as serialportss


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Send Data
def send_data(x, y):
    # 여러가지 방식의 값 송신 방법
    serialcomm.write(bytes(bytearray([0xC0])))
    serialcomm.write(bytes(bytearray([x])))
    serialcomm.write(bytes(bytearray([y])))


# Read Data
def read_data():
    # Packet에 시리얼을 통하여 입력된 값을 읽어온다.
    if serialcomm.inWaiting():
        packet = serialcomm.readline()

    # line return check
    if int(packet.decode('utf').rstrip('\n')) == 1:
        print('1')
    elif int(packet.decode('utf').rstrip('\n')) == 0:
        print('0')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # find port
    ports = list(serialportss.comports())
    for p in ports:
        print(p)

    print('Choose the serial port:')
    selport = input()

    # port OPEN
    serialcomm = serial.Serial()
    serialcomm.port = selport
    serialcomm.baudrate = 9600
    serialcomm.timeout = 0.5
    serialcomm.open()

    # date time 가져오기 (for filename)

    # file OPEN (r,w,a)
    f = open("C:/temp/001.txt", 'w')

    # Open Serial Comm.
    # ser = serial.Serial('COM1', 9600)

    # file closed.
    f.close()

    # serial port closed.
    serialcomm.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
