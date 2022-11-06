input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P13, 90)
})
input.onButtonPressed(Button.AB, function () {
    pins.servoWritePin(AnalogPin.P13, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P13, 180)
})
pins.servoWritePin(AnalogPin.P13, 0)
