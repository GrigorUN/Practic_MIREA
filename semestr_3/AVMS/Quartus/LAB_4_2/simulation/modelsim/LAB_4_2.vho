-- Copyright (C) 1991-2013 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- VENDOR "Altera"
-- PROGRAM "Quartus II 64-Bit"
-- VERSION "Version 13.1.0 Build 162 10/23/2013 SJ Web Edition"

-- DATE "12/09/2023 00:32:35"

-- 
-- Device: Altera EPM240F100C4 Package FBGA100
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY IEEE;
LIBRARY MAXII;
USE IEEE.STD_LOGIC_1164.ALL;
USE MAXII.MAXII_COMPONENTS.ALL;

ENTITY 	LAB_4_2 IS
    PORT (
	a : IN std_logic;
	b : IN std_logic;
	clock : IN std_logic;
	q : OUT std_logic_vector(3 DOWNTO 0)
	);
END LAB_4_2;

-- Design Ports Information
-- q[0]	=>  Location: PIN_C9,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[1]	=>  Location: PIN_E9,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[2]	=>  Location: PIN_C10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[3]	=>  Location: PIN_E8,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- b	=>  Location: PIN_E10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- clock	=>  Location: PIN_E1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- a	=>  Location: PIN_D10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default


ARCHITECTURE structure OF LAB_4_2 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_a : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL ww_clock : std_logic;
SIGNAL ww_q : std_logic_vector(3 DOWNTO 0);
SIGNAL \clock~combout\ : std_logic;
SIGNAL \b~combout\ : std_logic;
SIGNAL \a~combout\ : std_logic;
SIGNAL \newq[2]~8_combout\ : std_logic;
SIGNAL \newq[1]~4_combout\ : std_logic;
SIGNAL \newq[1]~6_combout\ : std_logic;
SIGNAL \newq[1]~0_combout\ : std_logic;
SIGNAL \newq[1]~5_combout\ : std_logic;
SIGNAL \newq[0]~1_combout\ : std_logic;
SIGNAL \newq[0]~2_combout\ : std_logic;
SIGNAL tq : std_logic_vector(3 DOWNTO 0);

BEGIN

ww_a <= a;
ww_b <= b;
ww_clock <= clock;
q <= ww_q;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: PIN_E1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\clock~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_clock,
	combout => \clock~combout\);

-- Location: PIN_E10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\b~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_b,
	combout => \b~combout\);

-- Location: PIN_D10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\a~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_a,
	combout => \a~combout\);

-- Location: LC_X6_Y3_N8
\newq[2]~8\ : maxii_lcell
-- Equation(s):
-- \newq[2]~8_combout\ = ((tq(1)) # ((\a~combout\ & !tq(3))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "f0fa",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \a~combout\,
	datac => tq(1),
	datad => tq(3),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[2]~8_combout\);

-- Location: LC_X6_Y3_N9
\tq[2]\ : maxii_lcell
-- Equation(s):
-- tq(2) = DFFEAS((tq(0) & ((\newq[2]~8_combout\ & (!tq(3))) # (!\newq[2]~8_combout\ & ((tq(2)))))) # (!tq(0) & (tq(3) $ ((tq(2))))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "36b4",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => tq(0),
	datab => tq(3),
	datac => tq(2),
	datad => \newq[2]~8_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => tq(2));

-- Location: LC_X6_Y3_N0
\newq[1]~4\ : maxii_lcell
-- Equation(s):
-- \newq[1]~4_combout\ = (!tq(0) & ((tq(2)) # ((!tq(1) & tq(3)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0d0c",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => tq(1),
	datab => tq(2),
	datac => tq(0),
	datad => tq(3),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[1]~4_combout\);

-- Location: LC_X6_Y3_N6
\newq[1]~6\ : maxii_lcell
-- Equation(s):
-- \newq[1]~6_combout\ = (tq(2)) # ((!tq(1) & (!\a~combout\ & tq(0))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "ff10",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => tq(1),
	datab => \a~combout\,
	datac => tq(0),
	datad => tq(2),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[1]~6_combout\);

-- Location: LC_X6_Y3_N3
\newq[1]~0\ : maxii_lcell
-- Equation(s):
-- \newq[1]~0_combout\ = (((tq(1) & !tq(2))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "00f0",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	datac => tq(1),
	datad => tq(2),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[1]~0_combout\);

-- Location: LC_X6_Y3_N4
\newq[1]~5\ : maxii_lcell
-- Equation(s):
-- \newq[1]~5_combout\ = (!\b~combout\ & (tq(3) & (tq(0) & \newq[1]~0_combout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "4000",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datab => tq(3),
	datac => tq(0),
	datad => \newq[1]~0_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[1]~5_combout\);

-- Location: LC_X6_Y3_N5
\tq[1]\ : maxii_lcell
-- Equation(s):
-- tq(1) = DFFEAS((\newq[1]~4_combout\) # ((\newq[1]~5_combout\) # ((!tq(3) & \newq[1]~6_combout\))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "ffdc",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => tq(3),
	datab => \newq[1]~4_combout\,
	datac => \newq[1]~6_combout\,
	datad => \newq[1]~5_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => tq(1));

-- Location: LC_X5_Y3_N4
\tq[3]\ : maxii_lcell
-- Equation(s):
-- tq(3) = DFFEAS((tq(1) & ((tq(2) & (!tq(3))) # (!tq(2) & ((!tq(0)))))) # (!tq(1) & (tq(3) $ (((tq(0)))))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "516e",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => tq(3),
	datab => tq(1),
	datac => tq(2),
	datad => tq(0),
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => tq(3));

-- Location: LC_X5_Y3_N7
\newq[0]~1\ : maxii_lcell
-- Equation(s):
-- \newq[0]~1_combout\ = (tq(1) & (tq(3) & (tq(0)))) # (!tq(1) & (tq(2) & (tq(3) $ (!tq(0)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "8890",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => tq(3),
	datab => tq(0),
	datac => tq(2),
	datad => tq(1),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[0]~1_combout\);

-- Location: LC_X5_Y3_N8
\newq[0]~2\ : maxii_lcell
-- Equation(s):
-- \newq[0]~2_combout\ = (tq(0) & ((tq(3)) # ((tq(2))))) # (!tq(0) & (tq(2) & (tq(3) $ (tq(1)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "d8e8",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => tq(3),
	datab => tq(0),
	datac => tq(2),
	datad => tq(1),
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \newq[0]~2_combout\);

-- Location: LC_X5_Y3_N9
\tq[0]\ : maxii_lcell
-- Equation(s):
-- tq(0) = DFFEAS((\b~combout\ & ((\newq[0]~2_combout\ & (!\newq[0]~1_combout\)) # (!\newq[0]~2_combout\ & ((\newq[1]~0_combout\))))) # (!\b~combout\ & ((\newq[1]~0_combout\) # (\newq[0]~1_combout\ $ (\newq[0]~2_combout\)))), GLOBAL(\clock~combout\), VCC, , 
-- , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "73f4",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \b~combout\,
	datab => \newq[0]~1_combout\,
	datac => \newq[1]~0_combout\,
	datad => \newq[0]~2_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => tq(0));

-- Location: PIN_C9,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[0]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => tq(0),
	oe => VCC,
	padio => ww_q(0));

-- Location: PIN_E9,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[1]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => tq(1),
	oe => VCC,
	padio => ww_q(1));

-- Location: PIN_C10,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[2]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => tq(2),
	oe => VCC,
	padio => ww_q(2));

-- Location: PIN_E8,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[3]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => tq(3),
	oe => VCC,
	padio => ww_q(3));
END structure;


