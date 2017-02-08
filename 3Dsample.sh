echo "Sampling from checkpoint lm_frac_$1.t7..."
if [ $2 == 'true' ]
	then
		th sample.lua cv/lm_frac_$1.t7 -gpuid -1 -length 196608
fi
echo "Sampling complete"
python3 3Darrangedata.py true
python3 texttoimage.py fractaloutput.txt 3D_$1
