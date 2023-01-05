x = 2
y = 2
led.plot(x, y)
basic.pause(1000)

def on_forever():
    global x, y
    if input.rotation(Rotation.ROLL) > 0:
        x += 1
    if input.rotation(Rotation.ROLL) < 0:
        x += -1
    if input.rotation(Rotation.PITCH) > 0:
        y += 1
    if input.rotation(Rotation.PITCH) < 0:
        y += -1
    if x > 4:
        x = 4
    if x < 0:
        x = 0
    if y > 4:
        y = 4
    if y < 0:
        y = 0
    led.plot(x, y)
    if x == 2 and y == 2:
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))    
    basic.pause(100)
    basic.clear_screen()
basic.forever(on_forever)

