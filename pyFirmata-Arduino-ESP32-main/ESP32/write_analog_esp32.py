from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')
it = util.Iterator(board)
it.start()

print('✔ board ready!')


def handle_write(*data):
    print(data)


board.add_cmd_handler(0x02, handle_write)


def writePwmValue(pin, value):
    datasToWrite = [pin, 0, 15, 10]

    v = divmod(value, 127)

    datasToWrite.extend(127 for _ in range(1, v[0]))
    if (v[0] >= 1):
        datasToWrite.append(v[1])
    else:
        datasToWrite.append(value)

    return datasToWrite


while True:
    board.send_sysex(0x04, writePwmValue(19, 1023))
    time.sleep(0.01)
