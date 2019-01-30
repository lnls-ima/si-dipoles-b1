#!/usr/bin/env bash

func=$1
cmd=$2
current=$3
side=$4


folder_src=x0-8p527mm
folder_dst=x0-8p527mm-reftraj


function create_pos {
  current=$1
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-002/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-003/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-004/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-005/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-006/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-009/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-010/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-011/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-012/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-013/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-014/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-015/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-016/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-017/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-018/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-019/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-020/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-021/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-022/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-023/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-024/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-025/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-026/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-027/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-028/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-029/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-030/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-031/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-032/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-033/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-034/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-035/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-036/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-037/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-038/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-039/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-040/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-041/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-042/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-043/$current/z-positive/
  cp ./$folder_src/trajectory-b1-pos.in ./$folder_dst/B1-046/$current/z-positive/
}


function create_neg {
  current=$1
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-002/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-003/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-004/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-005/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-006/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-009/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-010/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-011/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-012/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-013/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-014/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-015/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-016/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-017/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-018/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-019/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-020/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-021/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-022/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-023/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-024/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-025/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-026/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-027/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-028/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-029/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-030/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-031/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-032/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-033/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-034/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-035/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-036/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-037/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-038/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-039/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-040/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-041/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-042/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-043/$current/z-negative/
  cp ./$folder_src/trajectory-b1-neg.in ./$folder_dst/B1-046/$current/z-negative/
}


function replace_pos {
  current=$1
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-002/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-003/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-004/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-005/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-006/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-009/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-010/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-011/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-012/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-013/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-014/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-015/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-016/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-017/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-018/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-019/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-020/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-021/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-022/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-023/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-024/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-025/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-026/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-027/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-028/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-029/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-030/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-031/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-032/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-033/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-034/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-035/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-036/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-037/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-038/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-039/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-040/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-041/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-042/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-043/$current/z-positive/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-pos.in"/g' ./$folder_dst/B1-046/$current/z-positive/trajectory.in
}


function replace_neg {
  current=$1
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-002/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-003/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-004/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-005/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-006/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-009/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-010/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-011/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-012/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-013/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-014/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-015/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-016/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-017/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-018/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-019/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-020/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-021/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-022/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-023/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-024/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-025/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-026/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-027/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-028/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-029/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-030/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-031/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-032/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-033/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-034/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-035/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-036/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-037/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-038/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-039/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-040/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-041/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-042/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-043/$current/z-negative/trajectory.in
  sed -i 's/traj_load_filename            None/traj_load_filename "trajectory-b1-neg.in"/g' ./$folder_dst/B1-046/$current/z-negative/trajectory.in
}


# create_pos 381p7A
# create_neg 381p7A
# create_pos 401p8A
# create_neg 401p8A
create_pos 403p6A
create_neg 403p6A
# create_pos 421p9A
# create_neg 421p9A

# replace_pos 381p7A
# replace_neg 381p7A
# replace_pos 401p8A
# replace_neg 401p8A
replace_pos 403p6A
replace_neg 403p6A
# replace_pos 421p9A
# replace_neg 421p9A
