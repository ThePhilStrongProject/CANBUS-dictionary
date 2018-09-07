import serial
import re

version = "0.0.1"
ser = serial
mode = "debug"


def main():
    print("Phil's CAN dictionary")
    print("Version ", version, "\n")

    get_mode()

    while 1:
        d = " "
        if mode == "serial":
            d = serial_read()
        elif mode == "debug":
            d = input(">")
        parse_message(d)


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
        print("todo")


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
