onerror {exit -code 1}
vlib work
vlog -work work LAB_4.vo
vlog -work work Waveform3.vwf.vt
vsim -novopt -c -t 1ps -L maxii_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.LAB_4_vlg_vec_tst -voptargs="+acc"
vcd file -direction LAB_4.msim.vcd
vcd add -internal LAB_4_vlg_vec_tst/*
vcd add -internal LAB_4_vlg_vec_tst/i1/*
run -all
quit -f
