FROM python:2.7-alpine
MAINTAINER André Nishitani <atoshio25@gmail.com>

ARG N_JOBS=1

ENV QT_MAJOR 5
ENV QT_MINOR 7
ENV QT_BUILD 1
ENV QT_VERSION ${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}

ENV PATH $PATH:/opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/bin
ENV LD_LIBRARY_PATH /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/lib/pkgconfig:$PKG_CONFIG_PATH

ENV QT_FILE qt-everywhere-opensource-src-${QT_VERSION}.tar.xz

ENV QT_URL http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_VERSION}/single/$QT_FILE

RUN apk add --no-cache wget gcc cmake make g++ zlib-dev perl linux-headers \
    && cd /tmp \
    && wget -nc $QT_URL \
    && tar xf ${QT_FILE} \
    && cd /tmp/qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD} \
    && ./configure -prefix /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD} \
        -release \
        -opensource \
        -confirm-license \
        -shared \
        -no-qml-debug \
        -nomake examples \
        -no-opengl \
    && make -j${N_JOBS} && make install \
    && rm -r /tmp/qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}*

WORKDIR /

CMD ["qmake","--version"]
