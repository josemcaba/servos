def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P13, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.servo_write_pin(AnalogPin.P13, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P13, 180)
input.on_button_pressed(Button.B, on_button_pressed_b)

angulo = 0
