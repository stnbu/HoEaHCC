#!/bin/sh -ue

cd $(dirname "$0")

emacs README.org --batch -f org-html-export-to-html --kill
rsync -xva ./res ./README.html pu:/var/www/unintuitive.org/HoEaHCC/
echo "\n\n\nRefresh your browsers!\n\n\n"
mkdir -p build
mv -f ./README.html build/
git commit -am .
git push
