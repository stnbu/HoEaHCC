#!/bin/sh -ue

cd $(dirname "$0")

git commit -am .
git push
emacs README.org --batch -f org-html-export-to-html --kill
mkdir -p build
mv -f README.html build/
rsync -xva ./res ./build/README.html pu:/var/www/unintuitive.org/HoEaHCC/
