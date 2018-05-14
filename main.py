###########################################################
#       TRABALHO DE SISTEMAS OPERACIONAIS                 #
#  https://github.com/homdreen/memory-manager-simulator   #
#                                                         #
#   FELIPE HOMRICH MELCHIOR - LUCAS ANTUNES DE ALMEIDA    #
#         161150758                  161150753            #
########################################################### 

from interface import * # Importação da classe Interface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())
  