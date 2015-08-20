#!/bin/bash

set -e 

WORK_DIR=PolycloneInstall
BUNDLE=PolycloneInstall.zip

rm -f $BUNDLE
rm -rf $WORK_DIR

mkdir $WORK_DIR
mkdir $WORK_DIR/scripts
mkdir $WORK_DIR/polyclone
mkdir $WORK_DIR/polyclone/polyclone
mkdir $WORK_DIR/polyclone/polyclone/scripts

cp INSTALL $WORK_DIR
cp INSTALL_SCRIPTS $WORK_DIR/scripts
cp scripts/*.* $WORK_DIR/scripts

cp polyclone.wsgi $WORK_DIR/polyclone
cp polyclone.conf $WORK_DIR

cp -r *.py testfiles templates README.md requirements.txt $WORK_DIR/polyclone/polyclone

zip -r $BUNDLE $WORK_DIR

rm -rf $WORK_DIR
