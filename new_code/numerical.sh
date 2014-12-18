#! /bin/bash

echo "numerical experiment of cls.py and main.py"
rm oursol/res.txt

for f in inst/*.dat
do
    echo "Processing $f file..."
    echo "   processing $f in main.py"
    touch oursol/res.txt
    echo "**********RESULT OF $f **************" >> oursol/res.txt
    python main.py -f $f >> oursol/res.txt
   # echo "   processing $f in cls.py"
   # python cls.py -f $f >> oursol/res.txt
    echo "successed!"
done

