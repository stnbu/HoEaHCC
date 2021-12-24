#!/bin/sh -ue

cd $(dirname "$0")

git commit -am .
emacs README.org --batch -f org-html-export-to-html --kill
mkdir -p build
rsync -xva ./res ./README.html pu:/var/www/unintuitive.org/HoEaHCC/
echo -e "\n\n\nRefresh your browsers!\n\n\n
mv -f ./README.html build/
git push
