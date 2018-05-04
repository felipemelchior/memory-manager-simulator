from interface import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    
    ex.PageHit()
    ex.PageMiss()
    
    #ex.PID(349)
    
    sys.exit(app.exec_())