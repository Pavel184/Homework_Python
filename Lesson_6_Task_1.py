# Pavel Krupenya
# Traffic light
import time

class TrafficLight:
    colour = ["Red", "Yellow", "Green", "Yellow"]
    def running(self):
        while True:
            for el in TrafficLight.colour:
                if el == "Red":
                    print("\033[30m\033[41m {}".format(el))
                    time.sleep(7)
                elif el == "Green":
                    print("\033[30m\033[42m {}".format(el))
                    time.sleep(7)
                else:
                    print("\033[30m\033[43m {}".format(el))
                    time.sleep(2)
a = TrafficLight()
a.running()

