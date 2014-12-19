#! /bin/bash

echo "numerical experiment of cls.py and main.py"
#rm oursol/res.txt
rm oursol/sim_sol.txt

for f in insts/*.dat
do
    echo "Processing $f file..."
    echo "   processing $f in main.py"
    touch oursol/sim_sol.txt
    echo "**********RESULT OF $f **************" >> oursol/sim.txt
    python main_sim.py -f $f >> oursol/sim_sol.txt
   # echo "   processing $f in cls.py"
   # python cls.py -f $f >> oursol/res.txt
    echo "successed!"
done

