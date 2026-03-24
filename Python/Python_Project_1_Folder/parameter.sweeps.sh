#!/bin/bash
# Assignment 2 - Parameter sweep driver code

mkdir $exp_dir
#cp heat.py $exp_dir
cpAnimation.py $exp_dir
#cp heatsrc.csv $exp_dir
cd $exp_dir

outfile =" "
echo "Initial Human pop, Final human pop,  Initial vampire pop, final vampire pp"
for human_pop in {10,40} ;do
   for vampire_pop in {..5{; do

       initial_human_count = "$human_pop"
       initial_vampire_count="$ vampire_pop"
       final_human_count="$((initial_human_count *3))"
       final_vampire_count=$(initial_human_count*5))"


        echo = "$initial_human_count, $initial_vampire_count,$final_human_count, $final_vampire_count" >> outfile

        done
done


echo "paramter sweep completed. "
