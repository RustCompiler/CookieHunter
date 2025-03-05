import json, os, platform, threading, sys, gc
from rand_string.rand_string import RandString
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QTextEdit, QDialog, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
try:
    KEYS = ["Result", "Windows"]
    ARG_SYS = QApplication(sys.argv)

    class _default_setting:
        def app_conf(self):
            try:self.create_result = os.mkdir(KEYS[0])
            except FileExistsError:pass

            if (platform.uname()[0] == KEYS[1]):pass
            else:return "Linux"

    class TWrite():
        def echo(data):print(data)



    def CookiesLine(data_from_line):
        parts = data_from_line.strip().split("\t")
        if len(parts) < 7:
            return None
        return {
            "domain": parts[0], "flag": parts[1], "path": parts[2], "secure": parts[3], "expiration": parts[4], "name": parts[5], "value": parts[6]
        }


    def TXTTOJSON(input_folder, output_folder):
        if not os.path.exists(output_folder): os.makedirs(output_folder)
        TXT_DATALIST = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
        for CookieID, txt_file in enumerate(TXT_DATALIST, start=1):
            input_file = os.path.join(input_folder, txt_file)
            output_file = os.path.join(output_folder, f"Browser-Cookie-{CookieID}.json") 
            cookies = []
            with open(input_file, "r", encoding="utf-8") as file:
                for line in file:
                    cookie = CookiesLine(line)
                    if cookie: cookies.append(cookie)
            with open(output_file, "w", encoding="utf-8") as json_file:
                json.dump(cookies, json_file, indent=4, ensure_ascii=False)


    class GraphicalUserInterface(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("COOKIE HUNTER TREE | github.com/RustCompiler")
            self.setFixedSize(900, 500)
            self.setStyleSheet("background-color:#222222;")
            self.setWindowIcon(QIcon('data/icons/app.ico'))
            self.font_ubuntu_mono = QFontDatabase.addApplicationFont('data/fonts/UbuntuMono-Regular.ttf')
            self.select_uf = QFontDatabase.applicationFontFamilies(self.font_ubuntu_mono)

            self.fild_main = QLabel("Cookie Hunter Version Single", self)
            self.fild_main.setFont(QFont(self.select_uf[0], 20))
            self.fild_main.setStyleSheet("color:white")
            self.fild_main.setGeometry(280, 30, 500, 30)
        
            self.ads = QLabel("Telegram : t.me/RustTraffic | # Real Time Traffic", self)
            self.ads.setFont(QFont(self.select_uf[0], 15))
            self.ads.setStyleSheet("color:#2973B2")
            self.ads.setGeometry(200, 0, 500, 30)

            self.putfile = QPushButton("SELECT LOGS", self)
            self.putfile.setFont(QFont(self.select_uf[0], 20))
            self.putfile.setStyleSheet("color:green")
            self.putfile.setGeometry(340, 80, 200, 40)
            self.putfile.clicked.connect(self.__defineGetfile)
            
            self.log_area = QTextEdit(self)
            self.log_area.setReadOnly(True)
            self.log_area.setFont(QFont(self.select_uf[0],12))
            self.log_area.setStyleSheet("color: white; background-color: #333;")
            self.log_area.setGeometry(100, 150, 700, 300)
        
        
        def __defineGetfile(self):
        
            self.GET_PATH = QFileDialog.getExistingDirectoryUrl().url().replace("file:///", "")
            if self.GET_PATH:
                self.RandomDir = RandString("uppercase",12)
                TXTTOJSON(self.GET_PATH, str("Result\\Result - ["+self.RandomDir+"]"))
                self.log_area.append("[ + ] - Convert Completed!\n[ + ] - Directory Name : Result/"+self.RandomDir+"\n.......................\n")
            else:
                self.log_area.append("[ ! ] - Faild Convert!\n[ ! ] - Error Type: I/O\n.......................\n")
                pass



    def _define_src():
        Window = GraphicalUserInterface()
        Window.show()
        sys.exit(ARG_SYS.exec())
            
    def OpenSource(C):
        SYS_OBJ = _default_setting()
        if (SYS_OBJ.app_conf() == "Linux"):
            TWrite.echo("\nSorry, this operating system is not supported.\nMaybe it will be added in a future update.\n")         
            
            # Anyone might be wondering why this is here?
            # Well, I'm a C programmer and I'm used to always freeing memory
            # But since this was a Python code test project, I wanted to use this command, which most of the site has likened to (trash) this command.
            gc.collect() 

            sys.exit()

        
        else:
            CREATE_JOB = threading.Thread(target=C)
            CREATE_JOB.start()
    OpenSource(_define_src())

except IndexError:
    create_error = open('error.log','w',encoding='utf-8')
    create_error.write('Need Folder ( data )\ndata -> fonts\ndata -> icons\nPlease Please place the data folder next to the exe file.\ngithub.com/RustCompiler\nTelegram : t.me/RustTraffic\n............')
    create_error.close()
    pass