git add -A
git commit -m $1
git push origin dev
git checkout master
git merge dev -m $1
git push origin master
git checkout dev
