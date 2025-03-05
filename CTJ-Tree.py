import json, os, platform, threading, sys, gc
from rand_string.rand_string import RandString
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QTextEdit, QProgressBar, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
try:
    KEYS = ["Result", "Windows"]
    ARG_SYS = QApplication(sys.argv)

    class _default_setting:
        def app_conf(self):
            try:
                self.create_result = os.mkdir(KEYS[0])
            except FileExistsError:
                pass

            if platform.uname()[0] == KEYS[1]:
                pass
            else:
                return "Linux"

    class TWrite():
        def echo(data):
            print(data)

    def CookiesLine(data_from_line):
        parts = data_from_line.strip().split("\t")
        if len(parts) < 7:
            return None
        return {
            "domain": parts[0], "flag": parts[1], "path": parts[2], "secure": parts[3], "expiration": parts[4], "name": parts[5], "value": parts[6]
        }

    def TXTTOJSON(input_folder, output_folder):
        if not os.path.exists(output_folder): 
            os.makedirs(output_folder)
        
        TXT_DATALIST = []
        
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".txt"):
                    TXT_DATALIST.append(os.path.join(root, file))
        
        total_files = len(TXT_DATALIST)
        for idx, txt_file in enumerate(TXT_DATALIST, start=1):
            output_file = os.path.join(output_folder, f"Browser-Cookie-{idx}.json")
            cookies = []
            
            try:
                with open(txt_file, "r", encoding="utf-8") as file:
                    for line in file:
                        cookie = CookiesLine(line)
                        if cookie:
                            cookies.append(cookie)
                
                with open(output_file, "w", encoding="utf-8") as json_file:
                    json.dump(cookies, json_file, indent=4, ensure_ascii=False)
            
            except UnicodeDecodeError:
                print(f"Skipping file {txt_file} due to Unicode error.")
                continue
            progress_value = (idx / total_files) * 100
            update_progress(progress_value)

    def update_progress(value):
        
        if hasattr(window, 'progress'):
            window.progress.setValue(int(value))
            QApplication.processEvents()

    class GraphicalUserInterface(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("COOKIE HUNTER TREE | github.com/RustCompiler")
            self.setFixedSize(900, 500)
            self.setStyleSheet("background-color:#222222;")
            self.setWindowIcon(QIcon('data/icons/app.ico'))
            self.font_ubuntu_mono = QFontDatabase.addApplicationFont('data/fonts/UbuntuMono-Regular.ttf')
            self.select_uf = QFontDatabase.applicationFontFamilies(self.font_ubuntu_mono)

            self.fild_main = QLabel("LOG HUNTER Version Tree", self)
            self.fild_main.setFont(QFont(self.select_uf[0], 20))
            self.fild_main.setStyleSheet("color:white")
            self.fild_main.setGeometry(300, 30, 500, 30)

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
            self.log_area.setGeometry(100, 150, 700, 250)

            self.progress = QProgressBar(self)
            self.progress.setGeometry(220, 440, 500, 30)
            self.progress.setMaximum(100)

        def __defineGetfile(self):
            self.GET_PATH = QFileDialog.getExistingDirectoryUrl().url().replace("file:///", "")

            if self.GET_PATH:
                self.progress.setValue(0)
                self.log_area.setText("[ + ] - Processing ...\n.......................\n")
                self.process_thread = threading.Thread(target=self.process_files, args=(self.GET_PATH,))
                self.process_thread.start()
            else:
                self.log_area.setText("No folder selected.")

        def process_files(self, input_folder):
            output_folder = str("Result\\Result - [" + RandString("uppercase", 12) + "]")
            TXTTOJSON(input_folder, output_folder)

            self.log_area.setText("[ + ] - Convert Complete!\n.......................\n")
            self.progress.setValue(100)

    def _define_src():
        global window
        window = GraphicalUserInterface()
        window.show()
        sys.exit(ARG_SYS.exec())

    def OpenSource(C):
        SYS_OBJ = _default_setting()
        if SYS_OBJ.app_conf() == "Linux":
            TWrite.echo("\nSorry, this operating system is not supported.\nMaybe it will be added in a future update.\n")
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