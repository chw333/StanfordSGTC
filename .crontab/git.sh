#crontab -e
# */30 * * * * bash /mnt/larsix/projects/NMD/hansun/.crontab/git.sh

###
#for github
## git remote add origin https://github.com/hanice/StanfordSGTC.git
## to be
### git remote add origin ssh://git@github.com/hanice/StanfordSGTC.git

cd /mnt/larsix/projects/NMD/hansun
git add *.py
git add *.sh
git add *.R
git commit -a -m 'hanice'
git push origin master
