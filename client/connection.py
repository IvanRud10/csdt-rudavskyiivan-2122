import serial
import serial.tools.list_ports
import sys
import json
from collections import defaultdict


def show_message(text1, text2):
    return print(f"{text1}, {text2}")


COM_PORT = ""
ports = list(serial.tools.list_ports.comports())
for port in ports:
    if "Arduino" in port.description:
        COM_PORT = port.device

if not COM_PORT:
    show_message("Error", "Can't find Arduino COM port.")
    sys.exit()

BOUDRATE = 230400
SERIAL_TIMEOUT = 0.05
SERIAL_PORT = serial.Serial(port=COM_PORT, baudrate=BOUDRATE, timeout=SERIAL_TIMEOUT)

SERVER_ROOT = {"start": "<server>", "end": "</server>"}


def get_serial_message(start, end, previous_message):
    serial_message = SERIAL_PORT.readline().decode("UTF-8").strip()
    if previous_message == "":
        message_list = []
        flow_status = False
        while True:
            serial_message = SERIAL_PORT.readline().decode("UTF-8")
            if start in serial_message:
                message_list.append(serial_message)
                flow_status = True

            if (flow_status == True) and (end in serial_message):
                message_list.append(serial_message)
                message_str = "".join(message_list)
                return message_str[
                    message_str.index(start) : message_str.index(end) + len(end)
                ]

            if flow_status == True:
                message_list.append(serial_message)
    elif serial_message == "":
        return previous_message
    else:
        return serial_message


def bin_to_dict(bin_text):
    def default_value():
        return "ERROR"

    bin_message_dict = json.loads(json.dumps((bin_string).decode()))["server"]
    bin_message_default_dict = defaultdict(default_value, bin_message_dict)
    return bin_message_default_dict


def send_serial_message(message):
    SERIAL_PORT.write(message.encode("UTF-8"))
