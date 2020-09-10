#!/usr/bin/env bash

func=$1
cmd=$2
current=$3
side=$4

folder=x0-8p527mm-reftraj

function f1 {
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

function f2 {
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

function f3 {
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

function fnew {
  cmd=$1
  current=$2
  side=$3
  cd $folder/B1-022-new/$current/$side; fac-fma-analysis.py $cmd; cd ../../../../
}
$func $cmd $current $side
