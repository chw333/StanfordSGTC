#crontab -e
# */30 * * * * bash /mnt/larsix/projects/NMD/hansun/.crontab/git.sh
cd /mnt/larsix/projects/NMD/hansun
git add *.py
git add *.sh
git add *.R
git commit -a -m 'hanice'
git push origin master
