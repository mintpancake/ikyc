# ikyc
* An Intelligent Know Your Customer (iKYC) banking system with database manipulation and facial ID login functions. 
## Intro

<div align=center><img src="https://raw.githubusercontent.com/mintpancake/gallery/main/images/ikyc0.png"/></div>

<div align=center><img src="https://raw.githubusercontent.com/mintpancake/gallery/main/images/ikyc1.png"/></div>

<div align=center><img src="https://raw.githubusercontent.com/mintpancake/gallery/main/images/ikyc2.png"/></div>

<div align=center><img src="https://raw.githubusercontent.com/mintpancake/gallery/main/images/ikyc3.png"/></div>

<div align=center><img src="https://raw.githubusercontent.com/mintpancake/gallery/main/images/ikyc4.png"/></div>

## Requirements
### Files
* Import `train.yml`
### Dependencies
* See `requirements.txt`
### Configuration procedures (with `anaconda3`)
1. `conda create -n 3278 python=3.8`
2. `conda activate 3278`
3. `pip install -r requirements.txt`
### Start MySQL
1. Run `PowerShell` or `cmd` as Administrator
2. `net start MySQL` (check MySQL service name in `services.msc`)
3. `mysql -u root -p`
4. `ALTER USER 'root'@'localhost' IDENTIFIED BY '123456'` (change password)
5. `source database.sql` (load database)
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
#### Creating windows
1. Create a subclass of the `StackedWindow` class.
2. Initiate the window
   1. `loadUi("example.ui", self)`
   2. Connect the slots (see below)
   3. Override `activate()` and `deactivate()` if necessary (for switching windows)
#### Initiating slots (for sending signals)
* `self.exampleButton.clicked.connect(exampleFunc)` or
* `self.exampleButton.clicked.connect(lambda: exampleFunc(exampleArgs))`
#### Switching windows
1. `winList.append(ExampleWindow())` (optional) 
2. `switch_to(idx)`, where `idx` should be predefined as a constant
* Caution: Do not create duplicate windows! 
