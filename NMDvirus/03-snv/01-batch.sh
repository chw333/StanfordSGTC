cd HCV
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../


cd HIV1
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../


cd HSV1
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../


cd KHSV
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../


cd RSV
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../

cd WNV
python 02-snp-filter.py
cd Annotation
sh 01-format.sh
sh 03-annovar.sh
python 04-stopgain.py
cd ../../
