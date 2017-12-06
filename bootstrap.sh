#!/bin/bash

BASE_IMAGE=("ubuntu:xenial")
QT_VERSION=("487" "571" "593")

for VERSION in "${QT_VERSION[@]}"
do
  FOLDER="${VERSION:0:1}.${VERSION:1:1}.${VERSION:2:1}"
  mkdir -p $FOLDER
  cat Dockerfile.template \
    | sed "s/\%BASE_IMAGE\%/$BASE_IMAGE/" \
    | sed "s/\%QT_VERSION_MAJOR\%/${VERSION:0:1}/" \
    | sed "s/\%QT_VERSION_MINOR\%/${VERSION:1:1}/" \
    | sed "s/\%QT_VERSION_BUILD\%/${VERSION:2:1}/" > $FOLDER/Dockerfile
  echo "Qt v$VERSION [ UPDATED ]"
done
