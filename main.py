import os

from PyQt5 import QtCore, QtGui, QtWidgets
from docx_exchange import change_table_text
import subprocess


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 739)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_one = QtWidgets.QWidget()
        self.page_one.setObjectName("page_one")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_one)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_one)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 737))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.first_page_headerl_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.first_page_headerl_frame.setMinimumSize(QtCore.QSize(300, 50))
        self.first_page_headerl_frame.setMaximumSize(QtCore.QSize(300, 50))
        self.first_page_headerl_frame.setStyleSheet("#first_page_headerl_frame{\n"
                                                    "    background-color: white;\n"
                                                    "    border-radius: 10px;\n"
                                                    "    border-box: 2px solid black;\n"
                                                    "    box-shadow: 5px 5px 5px grey;\n"
                                                    "}")
        self.first_page_headerl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_page_headerl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_page_headerl_frame.setObjectName("first_page_headerl_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.first_page_headerl_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.first_page_header = QtWidgets.QLabel(self.first_page_headerl_frame)
        self.first_page_header.setMinimumSize(QtCore.QSize(270, 0))
        self.first_page_header.setMaximumSize(QtCore.QSize(270, 16777215))
        self.first_page_header.setSizeIncrement(QtCore.QSize(200, 0))
        self.first_page_header.setStyleSheet("font-size: 15pt;\n"
                                             "font-family: \"Segoe UI\";")
        self.first_page_header.setObjectName("first_page_header")
        self.verticalLayout_4.addWidget(self.first_page_header, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.first_page_headerl_frame, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setStyleSheet("border: 2px solid white;\n"
                                "color: white;\n"
                                "")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.first_page_main_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.first_page_main_frame.setStyleSheet("")
        self.first_page_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_page_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_page_main_frame.setObjectName("first_page_main_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.first_page_main_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.first_page_main_layout = QtWidgets.QVBoxLayout()
        self.first_page_main_layout.setObjectName("first_page_main_layout")
        self.obj_name_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.obj_name_line.setFont(font)
        self.obj_name_line.setStyleSheet("margin: 5px;\n"
                                         "border: 1px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: black;\n"
                                         "font-family: \"Segoe UI\";\n"
                                         "font-size: 12pt;")
        self.obj_name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.obj_name_line.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.obj_name_line.setObjectName("obj_name_line")
        self.first_page_main_layout.addWidget(self.obj_name_line)
        self.obj_type_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.obj_type_line.setStyleSheet("margin: 5px;\n"
                                         "border: 1px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: black;\n"
                                         "font-family: \"Segoe UI\";\n"
                                         "font-size: 12pt;")
        self.obj_type_line.setAlignment(QtCore.Qt.AlignCenter)
        self.obj_type_line.setObjectName("obj_type_line")
        self.first_page_main_layout.addWidget(self.obj_type_line)
        self.address_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.address_line.setStyleSheet("margin: 5px;\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font-family: \"Segoe UI\";\n"
                                        "font-size: 12pt;")
        self.address_line.setAlignment(QtCore.Qt.AlignCenter)
        self.address_line.setObjectName("address_line")
        self.first_page_main_layout.addWidget(self.address_line)
        self.sphere_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.sphere_line.setStyleSheet("margin: 5px;\n"
                                       "border: 1px solid white;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: black;\n"
                                       "font-family: \"Segoe UI\";\n"
                                       "font-size: 12pt;")
        self.sphere_line.setAlignment(QtCore.Qt.AlignCenter)
        self.sphere_line.setObjectName("sphere_line")
        self.first_page_main_layout.addWidget(self.sphere_line)
        self.additional_sphere_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.additional_sphere_line.setStyleSheet("margin: 5px;\n"
                                                  "border: 1px solid white;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: black;\n"
                                                  "font-family: \"Segoe UI\";\n"
                                                  "font-size: 12pt;")
        self.additional_sphere_line.setAlignment(QtCore.Qt.AlignCenter)
        self.additional_sphere_line.setObjectName("additional_sphere_line")
        self.first_page_main_layout.addWidget(self.additional_sphere_line)
        self.subj_name_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.subj_name_line.setStyleSheet("margin: 5px;\n"
                                          "border: 1px solid white;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: black;\n"
                                          "font-family: \"Segoe UI\";\n"
                                          "font-size: 12pt;")
        self.subj_name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.subj_name_line.setObjectName("subj_name_line")
        self.first_page_main_layout.addWidget(self.subj_name_line)
        self.subj_address_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.subj_address_line.setStyleSheet("margin: 5px;\n"
                                             "border: 1px solid white;\n"
                                             "border-radius: 10px;\n"
                                             "border-color: black;\n"
                                             "font-family: \"Segoe UI\";\n"
                                             "font-size: 12pt;")
        self.subj_address_line.setAlignment(QtCore.Qt.AlignCenter)
        self.subj_address_line.setObjectName("subj_address_line")
        self.first_page_main_layout.addWidget(self.subj_address_line)
        self.post_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.post_line.setStyleSheet("margin: 5px;\n"
                                     "border: 1px solid white;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: black;\n"
                                     "font-family: \"Segoe UI\";\n"
                                     "font-size: 12pt;")
        self.post_line.setAlignment(QtCore.Qt.AlignCenter)
        self.post_line.setObjectName("post_line")
        self.first_page_main_layout.addWidget(self.post_line)
        self.post_name_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.post_name_line.setStyleSheet("margin: 5px;\n"
                                          "border: 1px solid white;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: black;\n"
                                          "font-family: \"Segoe UI\";\n"
                                          "font-size: 12pt;")
        self.post_name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.post_name_line.setObjectName("post_name_line")
        self.first_page_main_layout.addWidget(self.post_name_line)
        self.resp_name_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.resp_name_line.setStyleSheet("margin: 5px;\n"
                                          "border: 1px solid white;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: black;\n"
                                          "font-family: \"Segoe UI\";\n"
                                          "font-size: 12pt;")
        self.resp_name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.resp_name_line.setObjectName("resp_name_line")
        self.first_page_main_layout.addWidget(self.resp_name_line)
        self.struct_resp_line = QtWidgets.QLineEdit(self.first_page_main_frame)
        self.struct_resp_line.setStyleSheet("margin: 5px;\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font-family: \"Segoe UI\";\n"
                                            "font-size: 12pt;")
        self.struct_resp_line.setAlignment(QtCore.Qt.AlignCenter)
        self.struct_resp_line.setObjectName("struct_resp_line")
        self.first_page_main_layout.addWidget(self.struct_resp_line)
        self.verticalLayout_5.addLayout(self.first_page_main_layout)
        self.verticalLayout_3.addWidget(self.first_page_main_frame, 0, QtCore.Qt.AlignBottom)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setStyleSheet("border: 2px solid white;\n"
                                  "color: white;\n"
                                  "")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.first_page_buttons_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.first_page_buttons_frame.setStyleSheet("pushButton{\n"
                                                    "    background-color: black;\n"
                                                    "}")
        self.first_page_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_page_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_page_buttons_frame.setObjectName("first_page_buttons_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.first_page_buttons_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.first_page_clear_btn = QtWidgets.QPushButton(self.first_page_buttons_frame)
        self.first_page_clear_btn.setStyleSheet("#first_page_clear_btn{\n"
                                                "    height: 30px;\n"
                                                "    border: 1px solid grey;\n"
                                                "    border-radius: 10px;\n"
                                                "    background-color: white;\n"
                                                "    transition-duration: 1.5s;\n"
                                                "    font-family: \"Segoe UI\";\n"
                                                "    font-size: 10pt;\n"
                                                "}\n"
                                                "#first_page_clear_btn:hover{\n"
                                                "    background-color: rgb(255, 44, 44);\n"
                                                "    border-radius: 10px;\n"
                                                "    border: transparent;\n"
                                                "}")
        self.first_page_clear_btn.setObjectName("first_page_clear_btn")
        self.horizontalLayout.addWidget(self.first_page_clear_btn)
        self.first_page_save_btn = QtWidgets.QPushButton(self.first_page_buttons_frame)
        self.first_page_save_btn.setStyleSheet("#first_page_save_btn{\n"
                                               "    height: 30px;\n"
                                               "    border: 1px solid grey;\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: white;\n"
                                               "    transition-duration: 1.5s;\n"
                                               "    font-family: \"Segoe UI\";\n"
                                               "    font-size: 10pt;\n"
                                               "}\n"
                                               "#first_page_save_btn:hover{\n"
                                               "    \n"
                                               "    background-color: rgb(4, 208, 21);\n"
                                               "    border-radius: 10px;\n"
                                               "    border: transparent;\n"
                                               "}")
        self.first_page_save_btn.setObjectName("first_page_save_btn")
        self.horizontalLayout.addWidget(self.first_page_save_btn)
        self.first_page_next_btn = QtWidgets.QPushButton(self.first_page_buttons_frame)
        self.first_page_next_btn.setStyleSheet("#first_page_next_btn{\n"
                                               "    height: 30px;\n"
                                               "    border: 1px solid grey;\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: white;\n"
                                               "    transition-duration: 1.5s;\n"
                                               "    font-family: \"Segoe UI\";\n"
                                               "    font-size: 10pt;\n"
                                               "}\n"
                                               "#first_page_next_btn:hover{\n"
                                               "    \n"
                                               "    background-color: rgb(60, 122, 255);\n"
                                               "    border-radius: 10px;\n"
                                               "    border: transparent;\n"
                                               "}")
        self.first_page_next_btn.setObjectName("first_page_next_btn")
        self.horizontalLayout.addWidget(self.first_page_next_btn)
        self.verticalLayout_3.addWidget(self.first_page_buttons_frame, 0, QtCore.Qt.AlignBottom)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_one)
        self.page_two = QtWidgets.QWidget()
        self.page_two.setObjectName("page_two")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_two)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.page_two)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.second_page_header_frame = QtWidgets.QFrame(self.frame_4)
        self.second_page_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_page_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_page_header_frame.setObjectName("second_page_header_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.second_page_header_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.second_page_header_frame)
        self.label_2.setStyleSheet("    font-family: \"Segoe UI\";\n"
                                   "    font-size: 15pt;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_8.addWidget(self.second_page_header_frame)
        self.second_page_main_frame = QtWidgets.QFrame(self.frame_4)
        self.second_page_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_page_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_page_main_frame.setObjectName("second_page_main_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.second_page_main_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.second_page_main_grid = QtWidgets.QGridLayout()
        self.second_page_main_grid.setObjectName("second_page_main_grid")
        self.order_number_label = QtWidgets.QLabel(self.second_page_main_frame)
        self.order_number_label.setStyleSheet("    font-family: \"Segoe UI\";\n"
                                              "    font-size: 10pt;")
        self.order_number_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_number_label.setObjectName("order_number_label")
        self.second_page_main_grid.addWidget(self.order_number_label, 0, 0, 1, 1)
        self.order_date_label = QtWidgets.QLabel(self.second_page_main_frame)
        self.order_date_label.setStyleSheet("    font-family: \"Segoe UI\";\n"
                                            "    font-size: 10pt;")
        self.order_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date_label.setObjectName("order_date_label")
        self.second_page_main_grid.addWidget(self.order_date_label, 1, 0, 1, 1)
        self.order_number_line = QtWidgets.QLineEdit(self.second_page_main_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.order_number_line.setFont(font)
        self.order_number_line.setStyleSheet("margin: 5px;\n"
                                             "border: 1px solid white;\n"
                                             "border-radius: 10px;\n"
                                             "border-color: black;\n"
                                             "    font-family: \"Segoe UI\";\n"
                                             "    font-size: 12pt;")
        self.order_number_line.setAlignment(QtCore.Qt.AlignCenter)
        self.order_number_line.setObjectName("order_number_line")
        self.second_page_main_grid.addWidget(self.order_number_line, 0, 1, 1, 1)
        self.order_date_line = QtWidgets.QLineEdit(self.second_page_main_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.order_date_line.setFont(font)
        self.order_date_line.setStyleSheet("margin: 5px;\n"
                                           "border: 1px solid white;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 12pt;")
        self.order_date_line.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date_line.setObjectName("order_date_line")
        self.second_page_main_grid.addWidget(self.order_date_line, 1, 1, 1, 1)
        self.city_label = QtWidgets.QLabel(self.second_page_main_frame)
        self.city_label.setStyleSheet("    font-family: \"Segoe UI\";\n"
                                      "    font-size: 10pt;")
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.second_page_main_grid.addWidget(self.city_label, 2, 0, 1, 1)
        self.city_line = QtWidgets.QLineEdit(self.second_page_main_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.city_line.setFont(font)
        self.city_line.setStyleSheet("margin: 5px;\n"
                                     "border: 1px solid white;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: black;\n"
                                     "    font-family: \"Segoe UI\";\n"
                                     "    font-size: 12pt;")
        self.city_line.setAlignment(QtCore.Qt.AlignCenter)
        self.city_line.setObjectName("city_line")
        self.second_page_main_grid.addWidget(self.city_line, 2, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.second_page_main_grid)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_comission_header_button = QtWidgets.QPushButton(self.second_page_main_frame)
        self.add_comission_header_button.setStyleSheet("#add_comission_header_button{\n"
                                                       "    height: 30px;\n"
                                                       "    border: 1px solid grey;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: white;\n"
                                                       "    transition-duration: 1.5s;\n"
                                                       "    font-family: \"Segoe UI\";\n"
                                                       "    font-size: 10pt;\n"
                                                       "}\n"
                                                       "#add_comission_header_button:hover{\n"
                                                       "    \n"
                                                       "    background-color: rgb(170, 255, 0);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    border: transparent;\n"
                                                       "}")
        self.add_comission_header_button.setObjectName("add_comission_header_button")
        self.horizontalLayout_2.addWidget(self.add_comission_header_button)
        self.add_comission_button = QtWidgets.QPushButton(self.second_page_main_frame)
        self.add_comission_button.setStyleSheet("#add_comission_button{\n"
                                                "    height: 30px;\n"
                                                "    border: 1px solid grey;\n"
                                                "    border-radius: 10px;\n"
                                                "    background-color: white;\n"
                                                "    transition-duration: 1.5s;\n"
                                                "    font-family: \"Segoe UI\";\n"
                                                "    font-size: 10pt;\n"
                                                "}\n"
                                                "#add_comission_button:hover{\n"
                                                "    \n"
                                                "    background-color: rgb(170, 255, 0);\n"
                                                "    border-radius: 10px;\n"
                                                "    border: transparent;\n"
                                                "}")
        self.add_comission_button.setObjectName("add_comission_button")
        self.horizontalLayout_2.addWidget(self.add_comission_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.del_comission_header_button = QtWidgets.QPushButton(self.second_page_main_frame)
        self.del_comission_header_button.setStyleSheet("#del_comission_header_button{\n"
                                                       "    height: 30px;\n"
                                                       "    border: 1px solid grey;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background-color: white;\n"
                                                       "    transition-duration: 1.5s;\n"
                                                       "    font-family: \"Segoe UI\";\n"
                                                       "    font-size: 10pt;\n"
                                                       "}\n"
                                                       "#del_comission_header_button:hover{\n"
                                                       "    background-color: rgb(255, 44, 44);\n"
                                                       "    border-radius: 10px;\n"
                                                       "    border: transparent;\n"
                                                       "}")
        self.del_comission_header_button.setObjectName("del_comission_header_button")
        self.horizontalLayout_3.addWidget(self.del_comission_header_button)
        self.del_comission_button = QtWidgets.QPushButton(self.second_page_main_frame)
        self.del_comission_button.setStyleSheet("#del_comission_button{\n"
                                                "    height: 30px;\n"
                                                "    border: 1px solid grey;\n"
                                                "    border-radius: 10px;\n"
                                                "    background-color: white;\n"
                                                "    transition-duration: 1.5s;\n"
                                                "    font-family: \"Segoe UI\";\n"
                                                "    font-size: 10pt;\n"
                                                "}\n"
                                                "#del_comission_button:hover{\n"
                                                "    background-color: rgb(255, 44, 44);\n"
                                                "    border-radius: 10px;\n"
                                                "    border: transparent;\n"
                                                "}    ")
        self.del_comission_button.setObjectName("del_comission_button")
        self.horizontalLayout_3.addWidget(self.del_comission_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_8.addWidget(self.second_page_main_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.second_page_buttons_frame_2 = QtWidgets.QFrame(self.frame_4)
        self.second_page_buttons_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_page_buttons_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_page_buttons_frame_2.setObjectName("second_page_buttons_frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.second_page_buttons_frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.create_act_button = QtWidgets.QPushButton(self.second_page_buttons_frame_2)
        self.create_act_button.setStyleSheet("#create_act_button{\n"
                                             "    height: 30px;\n"
                                             "    border: 1px solid grey;\n"
                                             "    border-radius: 10px;\n"
                                             "    background-color: white;\n"
                                             "    transition-duration: 1.5s;\n"
                                             "    font-family: \"Segoe UI\";\n"
                                             "    font-size: 10pt;\n"
                                             "}\n"
                                             "#create_act_button:hover{\n"
                                             "    \n"
                                             "    background-color: rgb(170, 255, 0);\n"
                                             "    border-radius: 10px;\n"
                                             "    border: transparent;\n"
                                             "}")
        self.create_act_button.setObjectName("create_act_button")
        self.horizontalLayout_6.addWidget(self.create_act_button)
        self.create_order_button = QtWidgets.QPushButton(self.second_page_buttons_frame_2)
        self.create_order_button.setStyleSheet("#create_order_button{\n"
                                               "    height: 30px;\n"
                                               "    border: 1px solid grey;\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: white;\n"
                                               "    transition-duration: 1.5s;\n"
                                               "    font-family: \"Segoe UI\";\n"
                                               "    font-size: 10pt;\n"
                                               "}\n"
                                               "#create_order_button:hover{\n"
                                               "    \n"
                                               "    background-color: rgb(170, 255, 0);\n"
                                               "    border-radius: 10px;\n"
                                               "    border: transparent;\n"
                                               "}")
        self.create_order_button.setObjectName("create_order_button")
        self.horizontalLayout_6.addWidget(self.create_order_button)
        self.verticalLayout_8.addWidget(self.second_page_buttons_frame_2)
        self.second_page_buttons_frame = QtWidgets.QFrame(self.frame_4)
        self.second_page_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_page_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_page_buttons_frame.setObjectName("second_page_buttons_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.second_page_buttons_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.second_page_clear_button = QtWidgets.QPushButton(self.second_page_buttons_frame)
        self.second_page_clear_button.setStyleSheet("#second_page_clear_button{\n"
                                                    "    height: 30px;\n"
                                                    "    border: 1px solid grey;\n"
                                                    "    border-radius: 10px;\n"
                                                    "    background-color: white;\n"
                                                    "    transition-duration: 1.5s;\n"
                                                    "    font-family: \"Segoe UI\";\n"
                                                    "    font-size: 10pt;\n"
                                                    "}\n"
                                                    "#second_page_clear_button:hover{\n"
                                                    "    background-color: rgb(255, 44, 44);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    border: transparent;\n"
                                                    "}")
        self.second_page_clear_button.setObjectName("second_page_clear_button")
        self.horizontalLayout_4.addWidget(self.second_page_clear_button)
        self.second_page_back_button = QtWidgets.QPushButton(self.second_page_buttons_frame)
        self.second_page_back_button.setStyleSheet("#second_page_back_button{\n"
                                                   "    height: 30px;\n"
                                                   "    border: 1px solid grey;\n"
                                                   "    border-radius: 10px;\n"
                                                   "    background-color: white;\n"
                                                   "    transition-duration: 1.5s;\n"
                                                   "    font-family: \"Segoe UI\";\n"
                                                   "    font-size: 10pt;\n"
                                                   "}\n"
                                                   "#second_page_back_button:hover{\n"
                                                   "    \n"
                                                   "    background-color: rgb(255, 17, 17);\n"
                                                   "    border-radius: 10px;\n"
                                                   "    border: transparent;\n"
                                                   "}")
        self.second_page_back_button.setObjectName("second_page_back_button")
        self.horizontalLayout_4.addWidget(self.second_page_back_button)
        self.second_page_next_button = QtWidgets.QPushButton(self.second_page_buttons_frame)
        self.second_page_next_button.setStyleSheet("#second_page_next_button{\n"
                                                   "    height: 30px;\n"
                                                   "    border: 1px solid grey;\n"
                                                   "    border-radius: 10px;\n"
                                                   "    background-color: white;\n"
                                                   "    transition-duration: 1.5s;\n"
                                                   "    font-family: \"Segoe UI\";\n"
                                                   "    font-size: 10pt;\n"
                                                   "}\n"
                                                   "#second_page_next_button:hover{\n"
                                                   "    \n"
                                                   "    background-color: rgb(60, 122, 255);\n"
                                                   "    border-radius: 10px;\n"
                                                   "    border: transparent;\n"
                                                   "}")
        self.second_page_next_button.setObjectName("second_page_next_button")
        self.horizontalLayout_4.addWidget(self.second_page_next_button)
        self.verticalLayout_8.addWidget(self.second_page_buttons_frame)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page_two)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font-size: 15pt;\n"
                                 "font-family: \"Segoe UI\";")
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_2)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setStyleSheet("border: 2px solid white;\n"
                                  "color: white;\n"
                                  "")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_12.addWidget(self.line_3)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.obj_target = QtWidgets.QLineEdit(self.frame_3)
        self.obj_target.setStyleSheet("margin: 5px;\n"
                                      "border: 1px solid white;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: black;\n"
                                      "font-family: \"Segoe UI\";\n"
                                      "font-size: 12pt;")
        self.obj_target.setAlignment(QtCore.Qt.AlignCenter)
        self.obj_target.setObjectName("obj_target")
        self.verticalLayout_14.addWidget(self.obj_target)
        self.obj_architecture = QtWidgets.QLineEdit(self.frame_3)
        self.obj_architecture.setStyleSheet("margin: 5px;\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font-family: \"Segoe UI\";\n"
                                            "font-size: 12pt;")
        self.obj_architecture.setAlignment(QtCore.Qt.AlignCenter)
        self.obj_architecture.setObjectName("obj_architecture")
        self.verticalLayout_14.addWidget(self.obj_architecture)
        self.EWM_name = QtWidgets.QLineEdit(self.frame_3)
        self.EWM_name.setStyleSheet("margin: 5px;\n"
                                    "border: 1px solid white;\n"
                                    "border-radius: 10px;\n"
                                    "border-color: black;\n"
                                    "font-family: \"Segoe UI\";\n"
                                    "font-size: 12pt;")
        self.EWM_name.setAlignment(QtCore.Qt.AlignCenter)
        self.EWM_name.setObjectName("EWM_name")
        self.verticalLayout_14.addWidget(self.EWM_name)
        self.PO_name = QtWidgets.QLineEdit(self.frame_3)
        self.PO_name.setStyleSheet("margin: 5px;\n"
                                   "border: 1px solid white;\n"
                                   "border-radius: 10px;\n"
                                   "border-color: black;\n"
                                   "font-family: \"Segoe UI\";\n"
                                   "font-size: 12pt;")
        self.PO_name.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_name.setObjectName("PO_name")
        self.verticalLayout_14.addWidget(self.PO_name)
        self.PO_2_name = QtWidgets.QLineEdit(self.frame_3)
        self.PO_2_name.setStyleSheet("margin: 5px;\n"
                                     "border: 1px solid white;\n"
                                     "border-radius: 10px;\n"
                                     "border-color: black;\n"
                                     "font-family: \"Segoe UI\";\n"
                                     "font-size: 12pt;")
        self.PO_2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.PO_2_name.setObjectName("PO_2_name")
        self.verticalLayout_14.addWidget(self.PO_2_name)
        self.signal_category = QtWidgets.QLineEdit(self.frame_3)
        self.signal_category.setStyleSheet("margin: 5px;\n"
                                           "border: 1px solid white;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "font-family: \"Segoe UI\";\n"
                                           "font-size: 12pt;")
        self.signal_category.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_category.setObjectName("signal_category")
        self.verticalLayout_14.addWidget(self.signal_category)
        self.provider_name = QtWidgets.QLineEdit(self.frame_3)
        self.provider_name.setStyleSheet("margin: 5px;\n"
                                         "border: 1px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: black;\n"
                                         "font-family: \"Segoe UI\";\n"
                                         "font-size: 12pt;")
        self.provider_name.setAlignment(QtCore.Qt.AlignCenter)
        self.provider_name.setObjectName("provider_name")
        self.verticalLayout_14.addWidget(self.provider_name)
        self.bad_category = QtWidgets.QLineEdit(self.frame_3)
        self.bad_category.setStyleSheet("margin: 5px;\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font-family: \"Segoe UI\";\n"
                                        "font-size: 12pt;")
        self.bad_category.setAlignment(QtCore.Qt.AlignCenter)
        self.bad_category.setObjectName("bad_category")
        self.verticalLayout_14.addWidget(self.bad_category)
        self.life_threats = QtWidgets.QLineEdit(self.frame_3)
        self.life_threats.setStyleSheet("margin: 5px;\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font-family: \"Segoe UI\";\n"
                                        "font-size: 12pt;")
        self.life_threats.setAlignment(QtCore.Qt.AlignCenter)
        self.life_threats.setObjectName("life_threats")
        self.verticalLayout_14.addWidget(self.life_threats)
        self.injections_types = QtWidgets.QLineEdit(self.frame_3)
        self.injections_types.setStyleSheet("margin: 5px;\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font-family: \"Segoe UI\";\n"
                                            "font-size: 12pt;")
        self.injections_types.setAlignment(QtCore.Qt.AlignCenter)
        self.injections_types.setObjectName("injections_types")
        self.verticalLayout_14.addWidget(self.injections_types)
        self.security_methods = QtWidgets.QLineEdit(self.frame_3)
        self.security_methods.setStyleSheet("margin: 5px;\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font-family: \"Segoe UI\";\n"
                                            "font-size: 12pt;")
        self.security_methods.setAlignment(QtCore.Qt.AlignCenter)
        self.security_methods.setObjectName("security_methods")
        self.verticalLayout_14.addWidget(self.security_methods)
        self.security_methods_2 = QtWidgets.QLineEdit(self.frame_3)
        self.security_methods_2.setStyleSheet("margin: 5px;\n"
                                              "border: 1px solid white;\n"
                                              "border-radius: 10px;\n"
                                              "border-color: black;\n"
                                              "font-family: \"Segoe UI\";\n"
                                              "font-size: 12pt;\n"
                                              "")
        self.security_methods_2.setAlignment(QtCore.Qt.AlignCenter)
        self.security_methods_2.setObjectName("security_methods_2")
        self.verticalLayout_14.addWidget(self.security_methods_2)
        self.organization_methods = QtWidgets.QLineEdit(self.frame_3)
        self.organization_methods.setStyleSheet("margin: 5px;\n"
                                                "border: 1px solid white;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: black;\n"
                                                "font-family: \"Segoe UI\";\n"
                                                "font-size: 12pt;")
        self.organization_methods.setAlignment(QtCore.Qt.AlignCenter)
        self.organization_methods.setObjectName("organization_methods")
        self.verticalLayout_14.addWidget(self.organization_methods)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_12.addWidget(self.frame_3)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setStyleSheet("border: 2px solid white;\n"
                                  "color: white;\n"
                                  "")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_12.addWidget(self.line_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.third_page_clear_btn = QtWidgets.QPushButton(self.frame_5)
        self.third_page_clear_btn.setStyleSheet("#third_page_clear_btn{\n"
                                                "    height: 30px;\n"
                                                "    border: 1px solid grey;\n"
                                                "    border-radius: 10px;\n"
                                                "    background-color: white;\n"
                                                "    transition-duration: 1.5s;\n"
                                                "    font-family: \"Segoe UI\";\n"
                                                "    font-size: 10pt;\n"
                                                "}\n"
                                                "#third_page_clear_btn:hover{\n"
                                                "    background-color: rgb(255, 44, 44);\n"
                                                "    border-radius: 10px;\n"
                                                "    border: transparent;\n"
                                                "}")
        self.third_page_clear_btn.setObjectName("third_page_clear_btn")
        self.horizontalLayout_5.addWidget(self.third_page_clear_btn)
        self.create_table_btn = QtWidgets.QPushButton(self.frame_5)
        self.create_table_btn.setStyleSheet("#create_table_btn{\n"
                                            "    height: 30px;\n"
                                            "    border: 1px solid grey;\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: white;\n"
                                            "    transition-duration: 1.5s;\n"
                                            "    font-family: \"Segoe UI\";\n"
                                            "    font-size: 10pt;\n"
                                            "}\n"
                                            "#create_table_btn:hover{\n"
                                            "    \n"
                                            "    background-color: rgb(4, 208, 21);\n"
                                            "    border-radius: 10px;\n"
                                            "    border: transparent;\n"
                                            "}")
        self.create_table_btn.setObjectName("create_table_btn")
        self.horizontalLayout_5.addWidget(self.create_table_btn)
        self.third_page_back_btn = QtWidgets.QPushButton(self.frame_5)
        self.third_page_back_btn.setStyleSheet("#third_page_back_btn{\n"
                                               "    height: 30px;\n"
                                               "    border: 1px solid grey;\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: white;\n"
                                               "    transition-duration: 1.5s;\n"
                                               "    font-family: \"Segoe UI\";\n"
                                               "    font-size: 10pt;\n"
                                               "}\n"
                                               "#third_page_back_btn:hover{\n"
                                               "    \n"
                                               "    background-color: red;\n"
                                               "    border-radius: 10px;\n"
                                               "    border: transparent;\n"
                                               "}")
        self.third_page_back_btn.setObjectName("third_page_back_btn")
        self.horizontalLayout_5.addWidget(self.third_page_back_btn)
        self.verticalLayout_12.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ADDING COMISSION

        self.del_comission_button.setEnabled(False)
        self.del_comission_header_button.setEnabled(False)
        self.dictionary = {}
        self.count = 0
        self.widgets_comission_name = []
        self.widgets_comission_post = []
        self.widgets_header = []
        self.widgets_comission = []
        self.comission = {}

        # ADDING/DELETING BUTTONS

        self.add_comission_button.clicked.connect(self.add_comission)
        self.del_comission_button.clicked.connect(self.del_comission)
        self.add_comission_header_button.clicked.connect(self.add_header)
        self.del_comission_header_button.clicked.connect(self.del_header)

        # MOVING SELECTORS

        self.first_page_next_btn.clicked.connect(self.first_page_next)
        self.second_page_back_button.clicked.connect(self.second_page_back)
        self.second_page_next_button.clicked.connect(self.second_page_next)
        self.third_page_back_btn.clicked.connect(self.third_page_back)

        # CREATING SELECTORS
        self.first_page_clear_btn.clicked.connect(self.clear_first_page)
        self.third_page_clear_btn.clicked.connect(self.clear_third_page)
        self.create_table_btn.clicked.connect(self.get_third_page_info)

    def add_header(self):
        self.del_comission_header_button.setEnabled(True)
        hor_layout = QtWidgets.QHBoxLayout()
        post_line = QtWidgets.QLabel("Председатель комиссии: ")
        name_line = QtWidgets.QLineEdit(placeholderText="Введите ФИО")
        hor_layout.addWidget(post_line)
        hor_layout.addWidget(name_line)
        self.widgets_header.append(name_line)
        self.verticalLayout_11.addLayout(hor_layout)
        self.add_comission_header_button.setEnabled(False)

    def del_header(self):
        self.add_comission_header_button.setEnabled(True)
        self.widgets_header[-1].deleteLater()
        del self.widgets_header[-1]
        self.del_comission_header_button.setEnabled(False)

    def add_comission(self):
        self.del_comission_button.setEnabled(True)
        horizont = QtWidgets.QHBoxLayout()
        self.count += 1
        num_line = QtWidgets.QLabel(f"{self.count}. ")
        name_line = QtWidgets.QLineEdit(placeholderText="Введите ФИО")
        post_line = QtWidgets.QLineEdit(placeholderText="Введите должность")
        horizont.addWidget(num_line)
        horizont.addWidget(name_line)
        horizont.addWidget(post_line)
        self.widgets_comission.append(horizont)
        self.widgets_comission_name.append(name_line)
        self.widgets_comission_post.append(post_line)
        self.verticalLayout_11.addLayout(horizont)

        if self.count == 10:
            self.add_comission_button.setEnabled(False)

    def del_comission(self):
        if self.count < 10:
            self.add_comission_button.setEnabled(True)
        self.widgets_comission[-1].deleteLater()
        self.count -= 1
        del self.widgets_comission[-1]

        if self.count < 1:
            self.del_comission_button.setEnabled(False)

    def get_comission_func(self):
        try:
            if len(self.widgets_comission_name) > 0 and len(self.widgets_comission_post) > 0:
                comission_list = []
                for i in range(len(self.widgets_comission_name)):
                    comission_list.append(f"{self.widgets_comission_name[i].text()}:{self.widgets_comission_post[i].text()}")
                self.comission.update(
                    {
                        "Председатель комиссии": f"{self.widgets_header[0].text()}",
                        "Члены комиссии": f"{comission_list}"
                    }
                )

                return self.comission
        except Exception as e:
            print(e)


    def get_third_page_info(self):
        self.dictionary.update(
            {
                "Назначение объекта": f"{self.obj_target.text()}",
                "Архитектура объекта": f"{self.obj_architecture.text()}",
                "Наименование ЭВМ": f"{self.EWM_name.text()}",
                "Наименование ПО": f"{self.PO_name.text()}",
                "Наименование прикладных ПО": f"{self.PO_2_name.text()}",
                "Категория сети электросвязи": f"{self.signal_category.text()}",
                "Наименование оператора связи": f"{self.provider_name.text()}",
                "Категория нарушителя": f"{self.bad_category.text()}",
                "Основные угрозы безопасности": f"{self.life_threats.text()}",
                "Типы компьютерных инцидентов": f"{self.injections_types.text()}",
                "Реализованные меры защиты": f"{self.security_methods.text()}",
                "Применяемые средства защиты": f"{self.security_methods_2.text()}",
                "Организационные меры": f"{self.organization_methods.text()}",
                "Наименование объекта": f"{self.obj_name_line.text()}",
                "Адрес размещения": f"{self.address_line.text()}",
                "Сфера деятельности": f"{self.sphere_line.text()}",
                "Тип объекта": f"{self.obj_type_line.text()}",
            }
        )
        change_table_text(dict=self.dictionary)
        os.startfile("Таблица категорирования.docx")

    def clear_third_page(self):
        self.obj_target.clear()
        self.obj_architecture.clear()
        self.EWM_name.clear()
        self.PO_name.clear()
        self.PO_2_name.clear()
        self.signal_category.clear()
        self.provider_name.clear()
        self.bad_category.clear()
        self.life_threats.clear()
        self.injections_types.clear()
        self.security_methods.clear()
        self.security_methods_2.clear()
        self.organization_methods.clear()

    def clear_first_page(self):
        self.obj_name_line.clear()
        self.obj_type_line.clear()
        self.address_line.clear()
        self.sphere_line.clear()
        self.additional_sphere_line.clear()
        self.subj_name_line.clear()
        self.subj_address_line.clear()
        self.post_line.clear()
        self.post_name_line.clear()
        self.resp_name_line.clear()
        self.struct_resp_line.clear()

    # MOVING SELECTORS

    def first_page_next(self):
        self.stackedWidget.setCurrentIndex(1)

    def second_page_next(self):
        self.get_comission_func()
        self.stackedWidget.setCurrentIndex(2)

    def second_page_back(self):
        self.stackedWidget.setCurrentIndex(0)

    def third_page_back(self):
        self.stackedWidget.setCurrentIndex(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.first_page_header.setText(_translate("MainWindow", "Характеристика объекта КИИ"))
        self.obj_name_line.setPlaceholderText(_translate("MainWindow", "Наименование объекта"))
        self.obj_type_line.setPlaceholderText(_translate("MainWindow", "Тип объекта"))
        self.address_line.setPlaceholderText(_translate("MainWindow", "Адрес местонахождения"))
        self.sphere_line.setPlaceholderText(_translate("MainWindow", "Сфера деятельности (основная)"))
        self.additional_sphere_line.setPlaceholderText(_translate("MainWindow", "Дополнительная сфера деятельности"))
        self.subj_name_line.setPlaceholderText(_translate("MainWindow", "Наименование субъекта"))
        self.subj_address_line.setPlaceholderText(
            _translate("MainWindow", "Адрес местонахождения субъекта (юридический адрес)"))
        self.post_line.setPlaceholderText(_translate("MainWindow", "Должность ответственного"))
        self.post_name_line.setPlaceholderText(_translate("MainWindow", "Инициалы и фамилия ответственного"))
        self.resp_name_line.setPlaceholderText(_translate("MainWindow", "ФИО ответственного лица"))
        self.struct_resp_line.setPlaceholderText(_translate("MainWindow", "Ответственное структурное подразделение"))
        self.first_page_clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.first_page_save_btn.setText(_translate("MainWindow", "Сохранить"))
        self.first_page_next_btn.setText(_translate("MainWindow", "Далее"))
        self.label_2.setText(_translate("MainWindow", "Состав комиссии"))
        self.order_number_label.setText(_translate("MainWindow", "Приказ №:"))
        self.order_date_label.setText(_translate("MainWindow", "Дата приказа:"))
        self.order_number_line.setPlaceholderText(_translate("MainWindow", "Введите номер приказа"))
        self.order_date_line.setPlaceholderText(_translate("MainWindow", "Введите дату приказа"))
        self.city_label.setText(_translate("MainWindow", "Город:"))
        self.city_line.setPlaceholderText(_translate("MainWindow", "Введите город"))
        self.add_comission_header_button.setText(_translate("MainWindow", "Добавить председателя комиссии"))
        self.add_comission_button.setText(_translate("MainWindow", "Добавить члена комиссии"))
        self.del_comission_header_button.setText(_translate("MainWindow", "Удалить председателя комисии"))
        self.del_comission_button.setText(_translate("MainWindow", "Удалить члена комиссии"))
        self.create_act_button.setText(_translate("MainWindow", "Составить акт"))
        self.create_order_button.setText(_translate("MainWindow", "Составить приказ"))
        self.second_page_clear_button.setText(_translate("MainWindow", "Очистить"))
        self.second_page_back_button.setText(_translate("MainWindow", "Назад"))
        self.second_page_next_button.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\">Дополнительные характеристики</p><p align=\"center\">объекта КИИ</p></body></html>"))
        self.obj_target.setPlaceholderText(_translate("MainWindow", "Назначение объекта"))
        self.obj_architecture.setPlaceholderText(_translate("MainWindow", "Архитектура объекта"))
        self.EWM_name.setPlaceholderText(_translate("MainWindow", "Наименование ЭВМ"))
        self.PO_name.setPlaceholderText(_translate("MainWindow", "Наименование ПО"))
        self.PO_2_name.setPlaceholderText(_translate("MainWindow", "Наименование прикладных ПО"))
        self.signal_category.setPlaceholderText(_translate("MainWindow", "Категория сети электросвязи"))
        self.provider_name.setPlaceholderText(_translate("MainWindow", "Наименование оператора связи"))
        self.bad_category.setPlaceholderText(_translate("MainWindow", "Категория нарушителя"))
        self.life_threats.setPlaceholderText(_translate("MainWindow", "Основные угрозы безопасности"))
        self.injections_types.setPlaceholderText(_translate("MainWindow", "Типы компьютерных инцидентов"))
        self.security_methods.setPlaceholderText(_translate("MainWindow", "Реализованные меры защиты"))
        self.security_methods_2.setPlaceholderText(_translate("MainWindow", "Применяемые средства защиты"))
        self.organization_methods.setPlaceholderText(_translate("MainWindow", "Организационные меры"))
        self.third_page_clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.create_table_btn.setText(_translate("MainWindow", "Составить таблицу"))
        self.third_page_back_btn.setText(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
