#!/bin/bash

BASE_IMAGE=("python:2.7-alpine")
QT_VERSION=("486" "571" "580" "593")

for VERSION in "${QT_VERSION[@]}"
do
    QT_FILE='qt-everywhere-opensource-src-${QT_VERSION}'
    QT_URL='http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_VERSION}'
    FOLDER="${VERSION:0:1}.${VERSION:1:1}.${VERSION:2:1}"
    mkdir -p $FOLDER
    if [ ${VERSION:0:1} -gt 4 ]
    then
        QT_FILE=${QT_FILE}".tar.xz"
        QT_URL=$QT_URL'/single/$QT_FILE'
    else
        QT_FILE=$QT_FILE".tar.gz"
        QT_URL=$QT_URL'/$QT_FILE'
    fi
    cat Dockerfile.template \
    | sed -e "s@\%BASE_IMAGE\%@$BASE_IMAGE@" \
    | sed -e "s@\%QT_VERSION_MAJOR\%@${VERSION:0:1}@" \
    | sed -e "s@\%QT_VERSION_MINOR\%@${VERSION:1:1}@" \
    | sed -e "s@\%QT_VERSION_BUILD\%@${VERSION:2:1}@" \
    | sed -e "s@\%QT_FILE\%@$QT_FILE@" \
    | sed -e "s@\%QT_URL\%@$QT_URL@" > $FOLDER/Dockerfile
    echo "Qt v$VERSION [ UPDATED ]"
done
