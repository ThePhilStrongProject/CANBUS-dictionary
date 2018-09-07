import serial
import re

version = "0.0.1"
ser = serial


def main():
    print("Phil's CAN dictionary")
    print("Version ", version, "\n")

    initiate_serial()

    ser.write(b'hello')  # write a string


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
    if ser.is_open:
        print("\nSuccessfully connected to ", ser.name)


main()