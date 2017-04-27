#!/bin/bash

UBUNTU_DISTRO=("trusty")
QT_VERSION=("487" "571" "580")

for VERSION in "${QT_VERSION[@]}"
do
  FOLDER="${VERSION:0:1}.${VERSION:1:1}.${VERSION:2:1}"
  rm $FOLDER
  mkdir $FOLDER
  cat Dockerfile.template \
    | sed "s/\%UBUNTU_DISTRO\%/$UBUNTU_DISTRO/" \
    | sed "s/\%QT_VERSION_MAJOR\%/${VERSION:0:1}/" \
    | sed "s/\%QT_VERSION_MINOR\%/${VERSION:1:1}/" \
    | sed "s/\%QT_VERSION_BUILD\%/${VERSION:2:1}/" > $FOLDER/Dockerfile
done
