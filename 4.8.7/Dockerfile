FROM ubuntu:trusty
MAINTAINER André Nishitani <atoshio25@gmail.com>

ENV QT_MAJOR 4
ENV QT_MINOR 8
ENV QT_BUILD 7

RUN apt-get update -y \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:beineri/opt-qt${QT_MAJOR}${QT_MINOR}${QT_BUILD}-$(lsb_release -sc) \
  && apt-get update \
  && apt-get install -y qt${QT_MAJOR}${QT_MINOR}-meta-full \
  && rm -rf /var/lib/apt/lists/* \
  && echo ". /opt/qt${QT_MAJOR}${QT_MINOR}/bin/qt${QT_MAJOR}${QT_MINOR}-env.sh" >> /etc/profile

CMD ["qmake","--version"]
