# ikyc
* This is an Intelligent
Know Your Customer (iKYC) system with facial ID login function.
## Requirements
### Packages
* `pyqt5`
* `pyqt5-tools`
* `opencv-python`
### Configuration procedures (with `anaconda3`)
1. `conda create -n 3278 python=3.8`
2. `conda activate 3278`
3. `pip install pyqt5`
4. `pip install pyqt5-tools`
5. `pip install opencv-python`
## Development guidelines
### Documentations
* https://www.figma.com/file/gKQlpgou7UHzjYl5jCZPiS/Customer-Journey
* https://drive.google.com/drive/folders/11_nJgVyp2L4RZMP-9o4Mvd1Pp2sOc8Dt
### Designing with `Qt Designer`
* Start `Qt Designer` (normally located at `%INSTALL_PATH%\anaconda3\envs\3278\Lib\site-packages\qt5_applications\Qt\bin\designer.exe`).
* Fix the window size  to `1200 x 800` and delete the menu bar and the status bar. 
* Rename every added `QObject` for future identification. 
* Customize styles with `styleSheet` under the `QWidget` property. 
  * Notice that relative paths used in `styleSheet` do not take effect in `Qt Designer` but essentially work fine. 
#### Color policy
* Themes:
  * `#8be5fd` (light blue in logo)
  * `#004094` (dark blue in logo)
* Backgrounds:
  * Windows: `#f7f6fb` (grey white)
  * Sections: `#ffffff` (white)
* Text: 
  * Titles: `#003780` (darker blue)
  * Main text: `#000000` (black)
  * Non-essential text: `#646464` (grey black)
* Buttons:
  * Light-color buttons: 
    * Normal: `HSV(hue, saturation, value)`
    * Hover: `HSV(hue, saturation, value - 10)`
    * Pressed: `HSV(hue, saturation, value - 20)`
  * Dark-color buttons: 
    * Normal: `HSV(hue, saturation, value)`
    * Hover: `HSV(hue, saturation, value + 15)`
    * Pressed: `HSV(hue, saturation, value)`
### Converting from `.ui` to `.py` (not necessary for coding)
1. `conda activate 3278`
2. `pyuic5 -x example.ui -o example.py`
### Coding
#### Loading `.ui` into `QMainWindow`
1. Include `from PyQt5.uic import loadUi`
2. Call `loadUi("example.ui", self)` in the constructor of a `QMainWindow`
#### Initiating slots (for sending signals)
* `self.exampleButton.clicked.connect(exampleFunc)` or
* `self.exampleButton.clicked.connect(lambda: exampleFunc(exampleArgs))`
#### Switching windows
* Already implemented by `switch_to(idx)` in `main.py`
1. `from PyQt5.QtWidgets import QStackedWidget`
2. `exampleWidget = QStackedWidget()`
3. `exampleWidget.addWidget(exampleWindow1)`
4. `exampleWidget.addWidget(exampleWindow2)`
5. `exampleWidget.setCurrentIndex(exampleIdx)`
#### To be continued...