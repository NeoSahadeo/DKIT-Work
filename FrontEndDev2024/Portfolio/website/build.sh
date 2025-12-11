#!/bin/bash

# Header
#
#		Purpose: Build and zip the site for upload to mysql
#		Author: Neo Sahadeo
#
# Body

rm oto.zip
pnpm run build
mv build oto
zip -r oto oto
rm -r ./oto
