FROM python:2.7-slim
MAINTAINER André Nishitani <atoshio25@gmail.com>

ARG N_JOBS=1

ENV QT_MAJOR 4
ENV QT_MINOR 5
ENV QT_BUILD 3
ENV QT_VERSION 4.5.3

ENV QT_BASE_DIR /opt/Qt/4.5.3

ENV PATH $PATH:/opt/Qt/4.5.3/bin
ENV LD_LIBRARY_PATH /opt/Qt/4.5.3/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH /opt/Qt/4.5.3/lib/pkgconfig:$PKG_CONFIG_PATH

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        build-essential wget \
    && cd /tmp \
    && wget -nv -nc https://download.qt.io/archive/qt/4.5/qt-embedded-linux-opensource-src-4.5.3.tar.gz \
    && tar xf qt-embedded-linux-opensource-src-4.5.3.tar.gz \
    && cd /tmp/qt-embedded-linux-opensource-src-4.5.3 \
    && ./configure -prefix /opt/Qt/4.5.3 \
        -release -opensource -confirm-license -shared -no-webkit -no-scripttools -nomake example -nomake demos \
    && make -j $N_JOBS && make install \
    && rm -r /tmp/qt-embedded-linux-opensource-src-4.5.3* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root

CMD ["qmake","--version"]