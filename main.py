import serial
import re

version = "0.0.1"
ser = serial
mode = "debug"
cantime = []
canid = []
candlc = []
candata0 = []
candata1 = []
candata2 = []
candata3 = []
candata4 = []
candata5 = []
candata6 = []
candata7 = []

def main():
    print("Phil's CAN dictionary tool")
    print("Version ", version, "\n")

    get_mode()

    while 1:
        d = " "
        if mode == "serial":
            d = serial_read()
        elif mode == "debug":
            d = input(">")
        parse_message(d)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\Time\tID\tDLC\tData[0]\tData[1]\tData[2]"
              "\tData[3]\tData[4]\tData[5]\tData[6]\tData[7]")
        for n in range(0,len(canid)):
            print(cantime[n], "\t", canid[n], "\t", candlc[n], "\t", candata0[n], "\t", candata1[n], "\t", candata2[n],
                  "\t", candata3[n], "\t", candata4[n], "\t", candata5[n], "\t", candata6[n], "\t", candata7[n])


def serial_read():
    return ser.readline()


def parse_message(s):
    if s.startswith("exit"):
        exit(0)
    elif s.startswith("mode"):
        get_mode()
    elif s.startswith("help"):
        print("exit, mode, help, can")
    elif s.startswith("can"):
        canread = s.split(';')
        if canread[1] in canid:
            pos = canid.index(canread[1])
            cantime[pos] = canread[2]
            candlc[pos] = canread[3]
            candata0[pos] = canread[4]
            candata1[pos] = canread[5]
            candata2[pos] = canread[6]
            candata3[pos] = canread[7]
            candata4[pos] = canread[8]
            candata5[pos] = canread[9]
            candata6[pos] = canread[10]
            candata7[pos] = canread[11]
        else:
            canid.append(canread[1])
            cantime.append(canread[2])
            candlc.append(canread[3])
            candata0.append(canread[4])
            candata1.append(canread[5])
            candata2.append(canread[6])
            candata3.append(canread[7])
            candata4.append(canread[8])
            candata5.append(canread[9])
            candata6.append(canread[10])
            candata7.append(canread[11])
    else:
        print("Not a valid command")


def error_handler(text="Error text not provided"):
    print(text)
    exit(1)


def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None


def initiate_serial():
    portinputtext = input("Enter COM port (eg. COM1):")
    portinputtext = portinputtext.strip()

    if portinputtext.startswith("COM"):
        port = get_trailing_number(portinputtext)
        if port is None:
            error_handler("Invalid COM port, exiting")
    else:
        error_handler("COM port not entered, exiting")

    ser = serial.Serial("COM" + str(port), 115200)
    ser.timeout = 1
    if ser.is_open:
        print("\nSuccessfully connected to ", ser.name)


def get_mode():
    modeinputtext = input("Select mode (debug/serial):")
    if modeinputtext == "debug":
        mode = "debug"
    elif modeinputtext == "serial":
        mode = "serial"
        initiate_serial()
    else:
        error_handler("Invalid mode")
    print("Selected mode: ", mode)


main()
