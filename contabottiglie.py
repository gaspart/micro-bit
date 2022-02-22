contatore = 0
basic.show_icon(IconNames.YES)
basic.pause(2000)

def on_forever():
    global contatore
    if sonar.ping(DigitalPin.P5, DigitalPin.P6, PingUnit.CENTIMETERS) > 3:
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.HEART)
        contatore += 1
        basic.pause(2000)
        basic.show_number(contatore)
        basic.pause(2000)
basic.forever(on_forever)
