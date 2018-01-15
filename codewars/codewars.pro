QT += core
QT -= gui

TARGET = codewars
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp
INCLUDEPATH += $$PWD/igloo-igloo.1.1.1/

CONFIG += c++14

HEADERS += \
    mycode.h \
    mytest.h

