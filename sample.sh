echo "Sampling from checkpoint lm_frac_$1.t7..."
if [ $2 == 'true' ]
	then
		th sample.lua cv/lm_frac_$1.t7 -gpuid -1 -length 65536
fi
echo "Sampling complete"
python3 arrangedata.py
python3 texttoimage.py fractaloutput.txt $1
