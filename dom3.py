class Robot:   
    def __init__(self, position):
        if position not in (11, 12, 13, 14):
            raise ValueError
        self.position = position
 
    def run_command(self, cmd):
        if cmd == 0:
            return
        elif cmd == -1:
            self.position -= 1
            if self.position < 11:
                self.position = 14
        elif cmd == 1:
            self.position += 1
            if self.position > 14:
                self.position = 11
        else:
            raise ValueError
        assert 11 <= self.position <= 14
 
    def __str__(self):
        return {
            11: 'North',
            12: 'West',
            13: 'South',
            14: 'East',
        }[self.position]
 
 
def main():
    print("Position: 11 = North, 12 = West, 13 = South, 14 = East")
    position = int(input("Enter first position: "))
    bot = Robot(position)
    while True:
        print("Command: 0 = continue movement, 1 = turn left, -1 = turn right")
        command = int(input("Enter command: "))
        bot.run_command(command)
        print(bot)
 
main()