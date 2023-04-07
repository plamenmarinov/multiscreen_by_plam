# multiscreen_by_plam
Simple multiscreen application

![python_kivy_logo](https://user-images.githubusercontent.com/117172634/230575424-c9956042-15b4-41ec-b9cd-def29120f67f.jpg)

![first](https://user-images.githubusercontent.com/117172634/230575960-d0502fb5-f4cc-4f4c-9849-3b305fdc6216.JPG)
![second](https://user-images.githubusercontent.com/117172634/230575951-c568bb7c-767c-4088-9891-8ae2426b4b06.JPG)
![third](https://user-images.githubusercontent.com/117172634/230575954-14ca6300-90c6-4c0c-b565-73cc5a490ffc.JPG)

This is a Python program that uses the Kivy library to create a multi-screen application. The code defines three screens, each represented by a separate class: FirstScreen, SecondScreen, and ThirdScreen. These screens are managed by a ScreenManager class, which is represented by the AppWindow class.

Each screen is defined in the Kivy language using the .kv file, which is loaded in the Python code using the Builder.load_file() method. Each screen has a layout with a label and one or two buttons. The buttons have text, font size, and background color attributes, and they have methods attached to them that define what happens when they are pressed.

The FirstScreen and SecondScreen both have a next() method that changes the current screen to the next screen, and sets the transition direction to "left". The SecondScreen and ThirdScreen both have a prev() method that changes the current screen to the previous screen, and sets the transition direction to "right".

The MultiScreenApp class is the main application class that is launched when the program is run. It simply returns the kv object, which contains the Kivy language definition of the screens. Finally, the if __name__ == '__main__': block creates an instance of the MultiScreenApp class, sets the title of the application, and runs it using the run() method.
