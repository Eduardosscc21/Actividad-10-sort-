
from wsgiref import headers
from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem,QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen,QColor,QTransform
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from administrador import Adminisrador
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.administrador=Adminisrador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(
            self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(
            self.click_agregar_inicio)
        self.ui.mostar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.ui.plainText_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.plainText_distancia_pushButton.clicked.connect(
            self.ordenar_distancia)
        self.ui.plainText_velocidad_pushButton.clicked.connect(
            self.ordenar_velocidad)

        self.ui.table_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.table_distancia_pushButton.clicked.connect(
            self.ordenar_distancia)

        self.ui.table_velocidad_pushButton.clicked.connect(
            self.ordenar_velocidad)

        self.scene=QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self,event):
            if event.delta() > 0:
                self.ui.graphicsView.scale(1.2,1.2)
            else:
                self.ui.graphicsView.scale(0.8,0.8)
                 
              

    
    @Slot()
    def ordenar_id(self):  # Manda a llamar un metodo que se encuentra en la clase administradora
        self.administrador.ordenar_ID()
        self.click_mostrar()
        self.mostrar_tabla()

    @Slot()
    # Manda a llamar un metodo que se encuentra en la clase administradora
    def ordenar_distancia(self):
        self.administrador.ordenar_DISTANCIA()
        self.click_mostrar()
        self.mostrar_tabla()

    @Slot()
    # Manda a llamar un metodo que se encuentra en la clase administradora
    def ordenar_velocidad(self):
        self.administrador.ordenar_VELOCIDAD()
        self.click_mostrar()
        self.mostrar_tabla()    


    @Slot()
    def dibujar(self):
       self.scene.clear()
       if len(self.administrador) > 0:
        pen=QPen()

        for particula in self.administrador:
            color=QColor(int(particula.red),int(particula.green),int(particula.blue))
            pen.setColor(color)

            dimension=4
            pen.setWidth(dimension)

            self.scene.addLine(particula.origen_x+3,particula.origen_y+3,particula.destino_x,particula.destino_y,pen)
            self.scene.addEllipse(particula.origen_x,
                                  particula.origen_y, dimension, dimension,pen)
            self.scene.addEllipse(particula.destino_x,
                                  particula.destino_y, dimension, dimension, pen)


    @Slot()
    def limpiar(self):
        self.scene.clear()


    @Slot()
    def buscar_id(self):
        #value
        id = self.ui.buscar_lineEdit.text()
        encontrado=False
        for particula in self.administrador:
            if id== particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)      
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado=True

                return
        if  not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el id "{id}" no fue encontrado'
            )        




    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id","Origen_x","Origen_y","Destino_x","Destino_y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.administrador))



        row=0
        for particula in self.administrador:

            id_widget = QTableWidgetItem(particula.id)      
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row+=1
            




    @Slot()
    def action_abrir_archivo(self):
        ubicacion=QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "se cargo el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )    
            

    
    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion=QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON(*.json)'
        )[0]
        print(ubicacion)
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )



    
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        distancia = self.ui.distancia_spinBox.value()

        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue,distancia)
        self.administrador.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        distancia = self.ui.distancia_spinBox.value()

        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue,distancia)
        self.administrador.agregar_inicio(particula)


      


        
