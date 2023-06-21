import speech_recognition as sr


class TV:
    """TV program."""

    def __init__(self):
        """Initialize TV with default settings."""
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        """Turn the TV on."""
        self.turned_on = True
        print("TV turned on.")

    def turn_off(self):
        """Turn the TV off."""
        self.turned_on = False
        print("TV turned off.")

    def process_voice_commands(self):
        """Process voice commands using speech recognition."""
        r = sr.Recognizer()

        while self.turned_on:
            with sr.Microphone() as source:
                print("Listening for voice commands")
                audio = r.listen(source)

            try:
                command = r.recognize_google(audio)
                print(f"Recognized voice command: {command}")
                self.process_command(command)

                if command.lower() == "tv off" or command.lower() == "turn off":
                    self.turn_off()
                    break
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the command.")
            except sr.RequestError:
                print("Sorry, I couldn't access the speech recognition service.")

    def process_command(self, command):
        """Process the given command."""
        command = command.lower()

        if "channel" in command:
            self.set_channel(command)
        elif "volume" in command:
            self.set_volume(command)
        elif "turn on" in command:
            self.turn_on()
        elif "turn off" in command:
            self.turn_off()
        else:
            print("Unknown command.")

    def set_channel(self, command):

        print("Channel changed.")

    def set_volume(self, command):
 
        print("Volume changed.")


def main():
    """Main program."""
    tv = TV()
    tv.turn_on()
    choice = input("Choose 'text' for text input, 'voice' for voice command: ")

    if choice.lower() == "text":
        while tv.turned_on:
            command = input("Please enter a command: ")
            tv.process_command(command)

            if command.lower() == "tv off" or command.lower() == "turn off":
                tv.turn_off()
                break
    elif choice.lower() == "voice":
        while tv.turned_on:
            tv.process_voice_commands()


if __name__ == "__main__":
    main()
