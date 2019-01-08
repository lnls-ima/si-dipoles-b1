#!/usr/bin/env bash

func=$1
cmd=$2
current=$3
side=$4

folder=x0-8p365mm

function f1 {
  cmd=$1
  current=$2
  side=$3
  cd $folder/B1-023/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-024/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-025/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-026/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-027/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-028/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-029/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-030/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-031/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-032/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../

}

function f2 {
  cmd=$1
  current=$2
  side=$3
  cd $folder/B1-002/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-003/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-004/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-005/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-006/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-009/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-010/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-011/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-012/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-013/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
}

function f3 {
  cmd=$1
  current=$2
  side=$3
  cd $folder/B1-014/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-015/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-016/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-017/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-018/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-019/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-020/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-021/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-022/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../

}

function f4 {
  cmd=$1
  current=$2
  side=$3
  cd $folder/B1-033/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-034/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-035/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-036/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-037/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-038/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-039/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-040/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-041/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-042/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-043/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
  cd $folder/B1-046/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
}

$func $cmd $current $side
#
# f1 run 381p7A z-positive >> log-381p7A-pos.txt &
# f2 run 381p7A z-positive >> log-381p7A-pos.txt &
# f3 run 381p7A z-positive >> log-381p7A-pos.txt &
# f4 run 381p7A z-positive >> log-381p7A-pos.txt &
# f1 run 381p7A z-negative >> log-381p7A-neg.txt &
# f2 run 381p7A z-negative >> log-381p7A-neg.txt &
# f3 run 381p7A z-negative >> log-381p7A-neg.txt &
# f4 run 381p7A z-negative >> log-381p7A-neg.txt &
# f1 run 401p8A z-positive >> log-401p8A-pos.txt &
# f2 run 401p8A z-positive >> log-401p8A-pos.txt &
# f3 run 401p8A z-positive >> log-401p8A-pos.txt &
# f4 run 401p8A z-positive >> log-401p8A-pos.txt &
# f1 run 401p8A z-negative >> log-401p8A-neg.txt &
# f2 run 401p8A z-negative >> log-401p8A-neg.txt &
# f3 run 401p8A z-negative >> log-401p8A-neg.txt &
# f4 run 401p8A z-negative >> log-401p8A-neg.txt &
# f1 run 403p6A z-positive >> log-403p6A-pos.txt &
# f2 run 403p6A z-positive >> log-403p6A-pos.txt &
# f3 run 403p6A z-positive >> log-403p6A-pos.txt &
# f4 run 403p6A z-positive >> log-403p6A-pos.txt &
# f1 run 403p6A z-negative >> log-403p6A-neg.txt &
# f2 run 403p6A z-negative >> log-403p6A-neg.txt &
# f3 run 403p6A z-negative >> log-403p6A-neg.txt &
# f4 run 403p6A z-negative >> log-403p6A-neg.txt &
# f1 run 421p9A z-positive >> log-421p9A-pos.txt &
# f2 run 421p9A z-positive >> log-421p9A-pos.txt &
# f3 run 421p9A z-positive >> log-421p9A-pos.txt &
# f4 run 421p9A z-positive >> log-421p9A-pos.txt &
# f1 run 421p9A z-negative >> log-421p9A-neg.txt &
# f2 run 421p9A z-negative >> log-421p9A-neg.txt &
# f3 run 421p9A z-negative >> log-421p9A-neg.txt &
# f4 run 421p9A z-negative >> log-421p9A-neg.txt &
#
#
# ./run-all.bash f1 run 381p7A z-positive
# ./run-all.bash f2 run 381p7A z-positive
# ./run-all.bash f3 run 381p7A z-positive
# ./run-all.bash f4 run 381p7A z-positive
# ./run-all.bash f1 run 381p7A z-negative
# ./run-all.bash f2 run 381p7A z-negative
# ./run-all.bash f3 run 381p7A z-negative
# ./run-all.bash f4 run 381p7A z-negative
# ./run-all.bash f1 run 401p8A z-positive
# ./run-all.bash f2 run 401p8A z-positive
# ./run-all.bash f3 run 401p8A z-positive
# ./run-all.bash f4 run 401p8A z-positive
# ./run-all.bash f1 run 401p8A z-negative
# ./run-all.bash f2 run 401p8A z-negative
# ./run-all.bash f3 run 401p8A z-negative
# ./run-all.bash f4 run 401p8A z-negative
# ./run-all.bash f1 run 403p6A z-positive
# ./run-all.bash f2 run 403p6A z-positive
# ./run-all.bash f3 run 403p6A z-positive
# ./run-all.bash f4 run 403p6A z-positive
# ./run-all.bash f1 run 403p6A z-negative
# ./run-all.bash f2 run 403p6A z-negative
# ./run-all.bash f3 run 403p6A z-negative
# ./run-all.bash f4 run 403p6A z-negative
# ./run-all.bash f1 run 421p9A z-positive
# ./run-all.bash f2 run 421p9A z-positive
# ./run-all.bash f3 run 421p9A z-positive
# ./run-all.bash f4 run 421p9A z-positive
# ./run-all.bash f1 run 421p9A z-negative
# ./run-all.bash f2 run 421p9A z-negative
# ./run-all.bash f3 run 421p9A z-negative
# ./run-all.bash f4 run 421p9A z-negative
