#  Auto Screenshot Tool


A simple Python automation tool that captures screenshots at fixed time intervals and saves them automatically.


---


##  Features


*  Captures screenshots automatically
*  Saves images to a user-defined folder
*  Supports formats like PNG and JPG
*  Customizable time interval
*  Lightweight and beginner-friendly


---


##  Installation
Clone the repository or download the project files:

```bash
git clone https://github.com/AsmitaTimalsena/auto_screenshot_taker_tool.git

```
Install required dependencies:
``` bash

pip install pyautogui
```
---
##  Usage

Run the following command in your project directory:


```bash
python main.py
```

Then provide the following inputs:
```bash

Enter the folder path where screenshots will be saved:
Enter the interval (in seconds) between screenshots:
Enter image format (png/jpg):

```

##  Example Output


```markdown
---------SCREENSHOT TAKER---------
Screenshot capturing started...
Screenshot saved: screen1.png
Screenshot saved: screen2.png
```
---


##  Project Structure


```
auto_screenshot_taker_tool/
│
├── screenshot_taker/
│   ├── __init__.py
│   └── main.py
│
├── pyproject.toml
├── setup.py
├── README.md

```


---


##  Contributing


Contributions are welcome!
Feel free to open issues or submit pull requests.


---


##  License


This project is licensed under the MIT License.


---


##  Author


Developed by Asmita Timalsena