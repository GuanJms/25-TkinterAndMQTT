"""
Using a fake robot as the receiver of messages.
"""

# TODO: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

""" A simple example of using MQTT for SENDING messages. """

import mqtt_remote_method_calls as com
import time
import tkinter
from tkinter import ttk


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    # while True:
    #     s = input("Enter a message: ")
    #     mqtt_client.send_message("say_it", [s])

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid()

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid()
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid()
    forward_button['command'] = lambda: mqtt_client.send_message("say_it", ["Forward",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<Up>', lambda event: mqtt_client.send_message("say_it", ["Forward",left_speed_entry.get(),left_speed_entry.get()]))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid()
    left_button['command'] = lambda: mqtt_client.send_message("say_it", ["Left",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<Left>', lambda event: mqtt_client.send_message("say_it", ["Left",left_speed_entry.get(),left_speed_entry.get()]))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid()
    stop_button['command'] = lambda: mqtt_client.send_message("say_it", ["Stop",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<space>', lambda event:mqtt_client.send_message("say_it", ["Stop",left_speed_entry.get(),left_speed_entry.get()]))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid()
    right_button['command'] = lambda: mqtt_client.send_message("say_it", ["Right",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<Right>', lambda event: mqtt_client.send_message("say_it", ["Right",left_speed_entry.get(),left_speed_entry.get()]))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid()
    back_button['command'] = lambda: mqtt_client.send_message("say_it", ["Back",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<Down>', lambda mqtt_client.send_message("say_it", ["Back",left_speed_entry.get(),left_speed_entry.get()]))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid()
    up_button['command'] = lambda:mqtt_client.send_message("say_it", ["Up",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<u>', lambda event: mqtt_client.send_message("say_it", ["Up",left_speed_entry.get(),left_speed_entry.get()]))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid()
    down_button['command'] = lambda:mqtt_client.send_message("say_it", ["Down",left_speed_entry.get(),left_speed_entry.get()])
    root.bind('<j>', lambda event: mqtt_client.send_message("say_it", ["Down",left_speed_entry.get(),left_speed_entry.get()]))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid()
    q_button['command'] = lambda: mqtt_client.send_message("say_it", ["Quit" ,left_speed_entry.get(),left_speed_entry.get()])

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid()
    e_button['command'] = lambda: exit()

    root.mainloop()


main()
