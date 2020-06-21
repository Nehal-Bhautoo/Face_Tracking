import time
from tkinter import *
import serial

RIGHT_LEFT_COUNTER = 90


class App:
    def __init__(self, master, ser):
        self.ser = ser
        self.button = Button(master, text="QUIT", fg="red", command=quit)
        self.button.grid(row=0, column=0, padx=0, pady=0, sticky="nw")
        self.slogan = Button(master, text="Reset", command=self.write_reset)
        self.slogan.grid(row=0, column=4, padx=0, pady=0, sticky="nw")
        self.Left = Button(master, text="←", padx=10, command=self.write_left)
        self.Left.grid(row=0, column=1, padx=0, pady=0, sticky="nw")
        self.Right = Button(master, text="→", padx=10, command=self.write_right)
        self.Right.grid(row=0, column=6, padx=2, pady=0, sticky="nw")
        self.sweep = Button(master, text="Sweep", command=self.write_sweep)
        self.sweep.grid(row=0, column=8, padx=0, pady=0, sticky="nw")

    # rotate servo to the left
    def write_left(self):
        global RIGHT_LEFT_COUNTER
        if RIGHT_LEFT_COUNTER > 0:
            RIGHT_LEFT_COUNTER -= 1
        self.ser.write(chr(RIGHT_LEFT_COUNTER))
        print(RIGHT_LEFT_COUNTER)
        print(self.ser.readline())

    # rotate servo to the right
    def write_right(self):
        global RIGHT_LEFT_COUNTER
        if RIGHT_LEFT_COUNTER < 180:
            RIGHT_LEFT_COUNTER += 1
        self.ser.write(chr(RIGHT_LEFT_COUNTER))
        print(RIGHT_LEFT_COUNTER)
        print(self.ser.readline())

    # reset servo at 90 degrees
    def write_reset(self):
        global RIGHT_LEFT_COUNTER
        RIGHT_LEFT_COUNTER = 90
        print(RIGHT_LEFT_COUNTER)
        self.ser.write(chr(RIGHT_LEFT_COUNTER))
        print(self.ser.readline())

    # sweep action for x-plane/horizontal servo
    def write_sweep(self):
        global RIGHT_LEFT_COUNTER
        for RIGHT_LEFT_COUNTER in range(0, 360):
            print(RIGHT_LEFT_COUNTER)
            self.ser.write(chr(RIGHT_LEFT_COUNTER))
            print(self.ser.readline())
            time.sleep(0.01)  # delays for 1 seconds
        RIGHT_LEFT_COUNTER = 90
        self.ser.write(chr(RIGHT_LEFT_COUNTER))


def main():
    ser = serial.Serial()
    ser.port = 'COM4'
    ser.baudrate = 9600
    ser.timeout = 0
    # open port if not already open
    if not ser.isOpen():
        ser.open()
    root = Tk()
    root.title("Servo Control")
    root.geometry("300x50+500+300")
    root.mainloop()


if __name__ == '__main__':
    main()
