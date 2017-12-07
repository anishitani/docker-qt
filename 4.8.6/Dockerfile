FROM python:2.7-alpine
MAINTAINER André Nishitani <atoshio25@gmail.com>

ARG N_JOBS=1

ENV QT_MAJOR 4
ENV QT_MINOR 8
ENV QT_BUILD 6
ENV QT_VERSION ${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}

ENV PATH $PATH:/opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/bin
ENV LD_LIBRARY_PATH /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH /opt/Qt/${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}/lib/pkgconfig:$PKG_CONFIG_PATH

ENV URL_QT5 http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_VERSION}/single/qt-everywhere-opensource-src-${QT_VERSION}.tar.xz
ENV URL_QT4 http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_VERSION}/qt-everywhere-opensource-src-${QT_VERSION}.tar.gz

RUN apk add --no-cache wget gcc cmake make g++ zlib-dev perl linux-headers \
    && cd /tmp \
    && if [ ${QT_MAJOR} -gt 4 ]; then wget -nc $URL_QT5; else then wget -nc $URL_QT4; fi
    && cd /tmp && tar xf qt-everywhere-opensource-src-${QT_MAJOR}.${QT_MINOR}.${QT_BUILD}.tar.xz \
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
