FROM python:2.7-slim
MAINTAINER André Nishitani <atoshio25@gmail.com>

ARG N_JOBS=1

ENV QT_MAJOR 5
ENV QT_MINOR 9
ENV QT_BUILD 3
ENV QT_VERSION 5.9.3

ENV QT_BASE_DIR /opt/Qt/5.9.3

ENV PATH $PATH:/opt/Qt/5.9.3/bin
ENV LD_LIBRARY_PATH /opt/Qt/5.9.3/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH /opt/Qt/5.9.3/lib/pkgconfig:$PKG_CONFIG_PATH

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        build-essential wget libgl1-mesa-dev libglu1-mesa-dev \
    && cd /tmp \
    && wget -nv -nc https://download.qt.io/archive/qt/5.9/5.9.3/single/qt-everywhere-opensource-src-5.9.3.tar.xz \
    && tar xf qt-everywhere-opensource-src-5.9.3.tar.xz \
    && cd /tmp/qt-everywhere-opensource-src-5.9.3 \
    && ./configure -prefix /opt/Qt/5.9.3 \
        -release -opensource -confirm-license -shared -no-qml-debug -nomake examples -opengl -qt-xcb \
    && make -j $N_JOBS && make install \
    && rm -r /tmp/qt-everywhere-opensource-src-5.9.3* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root

CMD ["qmake","--version"]