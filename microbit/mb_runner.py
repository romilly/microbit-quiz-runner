import radio

radio.on()
while True:
    incoming = radio.receive()
    if incoming:
        print(incoming)
