#!/usr/bin/env python

import jinja2
import os
import pprint

TEMPLATE_FILE = "Dockerfile.jinja"

class Version:
    _major = 5
    _minor = 9
    _build = 3

    def __init__(self, major=5, minor=9, build=3):
        self._major = major
        self._minor = minor
        self._build = build

    def toString(self):
        return '%d.%d.%d' % (self._major,self._minor,self._build)

class VersionConfiguration:
    _image = "python:2.7-slim"
    _version = Version()
    _dependencies = "build-essential wget"
    _options = ""
    _filename = ""
    _url = ""

    def __init__(self,
                 image = "python:2.7-slim",
                 version = Version(),
                 dependencies = "build-essential wget",
                 options = "-release -opensource -confirm-license -shared",
                 url = ""):
        self._image = image
        self._version = version
        self._dependencies = dependencies
        self._options = options
        self._url = url

    def templateVars(self):
        filename = self._url.split('/')[-1]
        folder = filename.split('.')[0]+'.'+filename.split('.')[1]+'.'+filename.split('.')[2]
        _vars = {
            "BASE_IMAGE":       self._image,
            "QT_VERSION":       self._version.toString(),
            "QT_VERSION_MAJOR": self._version._major,
            "QT_VERSION_MINOR": self._version._minor,
            "QT_VERSION_BUILD": self._version._build,
            "QT_DEPENDENCIES":  self._dependencies,
            "QT_BUILD_OPTIONS": self._options,
            "QT_URL":           self._url,
            "QT_FILE":          filename,
            "QT_SOURCE_FOLDER": folder
        }

        return _vars

    def prettyPrint(self):
        print 'Docker image:       ' + self._image
        print 'Build dependencies: ' + self._dependencies
        print 'Qt version:         ' + self._version.toString()
        print 'Configuration:      ' + self._options

def main():
    templateLoader = jinja2.FileSystemLoader( '.' )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( TEMPLATE_FILE )

    versionConfigurations = [
        VersionConfiguration(
            version=Version(4,5,3),
            options="-release -opensource -confirm-license -shared -no-webkit -no-scripttools -nomake example -nomake demos",
            url="https://download.qt.io/archive/qt/4.5/qt-embedded-linux-opensource-src-4.5.3.tar.gz"
        ),
        VersionConfiguration(
            version=Version(4,8,6),
            options="-release -opensource -confirm-license -shared -nomake examples -nomke demos -opengl",
            url="https://download.qt.io/archive/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tar.gz"
        ),
        VersionConfiguration(
            version=Version(5,7,1),
            options="-release -opensource -confirm-license -shared -nomake examples -nomke demos -opengl",
            url="https://download.qt.io/archive/qt/5.7/5.7.1/single/qt-everywhere-opensource-src-5.7.1.tar.gz"
        ),
        VersionConfiguration(
            version=Version(5,8,0),
            options="-release -opensource -confirm-license -shared -nomake examples -nomke demos -opengl",
            url="https://download.qt.io/archive/qt/5.8/5.8.0/single/qt-everywhere-opensource-src-5.8.0.tar.xz"
        ),
        VersionConfiguration(
            version=Version(5,9,3),
            options="-release -opensource -confirm-license -shared -nomake examples -nomke demos -opengl",
            url="https://download.qt.io/archive/qt/5.9/5.9.3/single/qt-everywhere-opensource-src-5.9.3.tar.xz"
        )
    ]

    for configuration in versionConfigurations:
        if not os.path.exists( configuration._version.toString() ):
            print "Creating directory " + configuration._version.toString()
            os.mkdir( configuration._version.toString() )
        else:
            print "Using directory " + configuration._version.toString()

        print "Writing new docker file with settings:"
        configuration.prettyPrint()

        dockerfile = open( configuration._version.toString()+"/Dockerfile", "w")
        dockerfile.write( template.render( configuration.templateVars() ).encode('utf-8') )
        dockerfile.close()

if __name__ == "__main__":
    main()

# BASE_IMAGE=("python:2.7-slim")
# QT_VERSION=("464" "486" "571" "580" "593")
#
# declare -A QT_OPTIONS
# QT_OPTIONS["464"]="-release -opensource -confirm-license -shared -nomake examples -opengl"
# QT_OPTIONS["486"]=${QT_OPTIONS["464"]}
# QT_OPTIONS["571"]="-release -opensource -confirm-license -shared -no-qml-debug -nomake examples -opengl -qt-xcb"
# QT_OPTIONS["580"]=${QT_OPTIONS["571"]}
# QT_OPTIONS["593"]=${QT_OPTIONS["571"]}
#
# for VERSION in "${QT_VERSION[@]}"
# do
#     QT_FILE='qt-everywhere-opensource-src-${QT_VERSION}'
#     QT_URL='http://download.qt.io/archive/qt/${QT_MAJOR}.${QT_MINOR}/${QT_VERSION}'
#     FOLDER="${VERSION:0:1}.${VERSION:1:1}.${VERSION:2:1}"
#     mkdir -p $FOLDER
#     if [ ${VERSION:0:1} -gt 4 ]
#     then
#         QT_FILE=${QT_FILE}".tar.xz"
#         QT_URL=$QT_URL'/single/$QT_FILE'
#     else
#         QT_FILE=$QT_FILE".tar.gz"
#         QT_URL=$QT_URL'/$QT_FILE'
#     fi
#     cat Dockerfile.template \
#     | sed -e "s@\%BASE_IMAGE\%@$BASE_IMAGE@" \
#     | sed -e "s@\%QT_VERSION_MAJOR\%@${VERSION:0:1}@" \
#     | sed -e "s@\%QT_VERSION_MINOR\%@${VERSION:1:1}@" \
#     | sed -e "s@\%QT_VERSION_BUILD\%@${VERSION:2:1}@" \
#     | sed -e "s@\%QT_FILE\%@$QT_FILE@" \
#     | sed -e "s@\%QT_URL\%@$QT_URL@" \
#     | sed -e "s@\%QT_OPTIONS\%@${QT_OPTIONS["486"]}@" > $FOLDER/Dockerfile
#     echo "Qt v$VERSION [ UPDATED ] with ${QT_OPTIONS[$VERSION]}"
# done
