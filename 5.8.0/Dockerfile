FROM ubuntu:xenial
MAINTAINER André Nishitani <atoshio25@gmail.com>

ENV QT_MAJOR 5
ENV QT_MINOR 8
ENV QT_BUILD 0

RUN apt-get update && apt-get install -y wget build-essential

RUN cd /tmp \
    && wget http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/single/qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}.tar.gz
RUN cd /tmp && tar -xzf qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}.tar.gz

WORKDIR /tmp/qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}

RUN ./configure -prefix /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD} \
    -release \
    -opensource \
    -confirm-license \
    -shared \
    -no-qml-debug \
    -nomake examples \
    -no-opengl
RUN make && make install

CMD ["qmake","--version"]
