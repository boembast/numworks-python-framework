from ui_classes import *

Text("Hello World", 10, 10, "Hello World", "black", "white")._draw()
Button("MyButton", 10, 50, "Click Me", "blue")._draw()
field = Input("MyInput", 10, 90, 200, 30, "green")
field.setText("Type Here :D")
field._draw()
toggle = Toggle("MyToggle", 10, 130, "Enable Feature", "orange")
toggle._draw()
while not ion.keydown(ion.KEY_OK): pass
toggle.state = not toggle.state
toggle._draw()