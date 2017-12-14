FROM python:2.7-slim
MAINTAINER André Nishitani <atoshio25@gmail.com>

ARG N_JOBS=1

ENV QT_MAJOR 4
ENV QT_MINOR 8
ENV QT_BUILD 6
ENV QT_VERSION 4.8.6

ENV QT_BASE_DIR /opt/Qt/4.8.6

ENV PATH $PATH:/opt/Qt/4.8.6/bin
ENV LD_LIBRARY_PATH /opt/Qt/4.8.6/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH /opt/Qt/4.8.6/lib/pkgconfig:$PKG_CONFIG_PATH

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        build-essential wget libgl1-mesa-dev libglu1-mesa-dev \
    && cd /tmp \
    && wget -nv -nc https://download.qt.io/archive/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tar.gz \
    && tar xf qt-everywhere-opensource-src-4.8.6.tar.gz \
    && cd /tmp/qt-everywhere-opensource-src-4.8.6 \
    && ./configure -prefix /opt/Qt/4.8.6 \
        -release -opensource -confirm-license -shared -nomake examples -nomake demos -opengl \
    && make -j $N_JOBS && make install \
    && rm -r /tmp/qt-everywhere-opensource-src-4.8.6* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root

CMD ["qmake","--version"]