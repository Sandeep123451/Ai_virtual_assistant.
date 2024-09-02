import sys
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
            print("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            print("Could not request results; check your network connection.")
        return ""

# Function to process text and voice commands
def process_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "open drive" in command:
        speak("Opening Google Drive")
        webbrowser.open("https://drive.google.com")
    elif "open file manager" in command or "open explorer" in command:
        speak("Opening File Manager")
        os.system("explorer")
    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")
    else:
        speak("Sorry, I don't understand that command.")
        print("Sorry, I don't understand that command.")

# Main class for the assistant's UI
class VirtualAssistant(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up the UI layout
        self.setWindowTitle('AI Virtual Assistant')
        self.setGeometry(100, 100, 400, 600)  # Same size as before

        # Add a cartoon image (example image, replace with your own)
        self.cartoon_label = QLabel(self)
        pixmap_cartoon = QPixmap("doreamonai.png")  # Replace with the path to your "Hi" cartoon image
        self.cartoon_label.setPixmap(pixmap_cartoon)
        self.cartoon_label.setScaledContents(True)
        self.cartoon_label.setAlignment(Qt.AlignCenter)
        self.cartoon_label.setFixedSize(500,300)  # Adjust size to make it bigger but fit within the window

        # Add buttons with styling
        self.ask_button = QPushButton('Ask', self)
        self.ask_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 10px;")
        self.ask_button.setFont(QFont("Arial", 14))
        self.ask_button.clicked.connect(self.ask)

        self.send_button = QPushButton('Send', self)
        self.send_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 18px; padding: 10px;")
        self.send_button.setFont(QFont("Arial", 14))
        self.send_button.clicked.connect(self.send)

        self.delete_button = QPushButton('Delete', self)
        self.delete_button.setStyleSheet("background-color: #f44336; color: white; font-size: 18px; padding: 10px;")
        self.delete_button.setFont(QFont("Arial", 14))
        self.delete_button.clicked.connect(self.clear_text)

        # Add a text input field
        self.text_input = QLineEdit(self)
        self.text_input.setFont(QFont("Arial", 14))
        self.text_input.setPlaceholderText("Type your command here...")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.cartoon_label)  # Cartoon image at the top

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ask_button)
        button_layout.addWidget(self.send_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)  # Buttons below the image
        layout.addWidget(self.text_input)  # Text input field at the bottom
        self.setLayout(layout)

    def ask(self):
        command = listen_command()
        if command:
            process_command(command)

    def send(self):
        command = self.text_input.text().lower()
        process_command(command)

    def clear_text(self):
        self.text_input.clear()

# Main function to run the assistant
def main():
    app = QApplication(sys.argv)
    assistant = VirtualAssistant()
    assistant.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

