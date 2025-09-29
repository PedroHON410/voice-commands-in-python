import sys
from PyQt6.QtWidgets import QApplication, QWidget
#Create the application
app = QApplication(sys.argv)

#Create the main window
window = QWidget()
window.resize(400, 300)
window.setWindowTitle("Voice Commands ")
window.show()

#Run the application event loop
sys.exit(app.exec())