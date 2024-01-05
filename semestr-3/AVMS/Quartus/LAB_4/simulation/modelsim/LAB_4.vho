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

-- DATE "12/08/2023 22:44:30"

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

ENTITY 	LAB_4 IS
    PORT (
	q : OUT std_logic_vector(3 DOWNTO 0);
	clock : IN std_logic;
	b : IN std_logic;
	a : IN std_logic
	);
END LAB_4;

-- Design Ports Information
-- q[3]	=>  Location: PIN_A1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[2]	=>  Location: PIN_B3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[1]	=>  Location: PIN_D3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[0]	=>  Location: PIN_B1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- clock	=>  Location: PIN_E1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- a	=>  Location: PIN_C2,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- b	=>  Location: PIN_C1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default


ARCHITECTURE structure OF LAB_4 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_q : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_clock : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL ww_a : std_logic;
SIGNAL \clock~combout\ : std_logic;
SIGNAL \b~combout\ : std_logic;
SIGNAL \a~combout\ : std_logic;
SIGNAL \inst24~8_combout\ : std_logic;
SIGNAL \inst24~11_combout\ : std_logic;
SIGNAL \inst31~regout\ : std_logic;
SIGNAL \inst23~4_combout\ : std_logic;
SIGNAL \inst33~regout\ : std_logic;
SIGNAL \inst25~4_combout\ : std_logic;
SIGNAL \inst29~regout\ : std_logic;
SIGNAL \inst27~regout\ : std_logic;

BEGIN

q <= ww_q;
ww_clock <= clock;
ww_b <= b;
ww_a <= a;
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

-- Location: PIN_C1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\b~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_b,
	combout => \b~combout\);

-- Location: PIN_C2,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\a~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_a,
	combout => \a~combout\);

-- Location: LC_X2_Y4_N5
\inst24~8\ : maxii_lcell
-- Equation(s):
-- \inst24~8_combout\ = (\inst31~regout\ & (!\b~combout\ & ((\inst27~regout\)))) # (!\inst31~regout\ & (((!\a~combout\ & !\inst27~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "5003",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datab => \a~combout\,
	datac => \inst31~regout\,
	datad => \inst27~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~8_combout\);

-- Location: LC_X2_Y4_N6
\inst24~11\ : maxii_lcell
-- Equation(s):
-- \inst24~11_combout\ = ((\inst33~regout\ & ((!\inst27~regout\))) # (!\inst33~regout\ & (!\inst31~regout\ & \inst27~regout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "03cc",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	datab => \inst33~regout\,
	datac => \inst31~regout\,
	datad => \inst27~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~11_combout\);

-- Location: LC_X2_Y4_N7
inst31 : maxii_lcell
-- Equation(s):
-- \inst31~regout\ = DFFEAS((\inst29~regout\ & (((\inst24~11_combout\)) # (!\inst33~regout\))) # (!\inst29~regout\ & ((\inst33~regout\ & (\inst24~8_combout\)) # (!\inst33~regout\ & ((\inst24~11_combout\))))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "fb62",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst29~regout\,
	datab => \inst33~regout\,
	datac => \inst24~8_combout\,
	datad => \inst24~11_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst31~regout\);

-- Location: LC_X2_Y4_N0
\inst23~4\ : maxii_lcell
-- Equation(s):
-- \inst23~4_combout\ = (\inst31~regout\ & (((!\inst33~regout\) # (!\b~combout\)) # (!\inst27~regout\))) # (!\inst31~regout\ & ((\inst33~regout\) # ((!\inst27~regout\ & !\b~combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "7fcd",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \inst31~regout\,
	datac => \b~combout\,
	datad => \inst33~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~4_combout\);

-- Location: LC_X2_Y4_N1
inst33 : maxii_lcell
-- Equation(s):
-- \inst33~regout\ = DFFEAS((\inst29~regout\ & ((\inst27~regout\ & (!\inst31~regout\ & !\inst23~4_combout\)) # (!\inst27~regout\ & ((\inst23~4_combout\))))) # (!\inst29~regout\ & (\inst23~4_combout\ & ((\inst27~regout\) # (\inst31~regout\)))), 
-- GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "7608",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst31~regout\,
	datad => \inst23~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst33~regout\);

-- Location: LC_X2_Y4_N2
\inst25~4\ : maxii_lcell
-- Equation(s):
-- \inst25~4_combout\ = (\inst27~regout\ & (((!\inst33~regout\)))) # (!\inst27~regout\ & (\inst33~regout\ & ((\a~combout\) # (\inst31~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "54aa",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \a~combout\,
	datac => \inst31~regout\,
	datad => \inst33~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst25~4_combout\);

-- Location: LC_X2_Y4_N3
inst29 : maxii_lcell
-- Equation(s):
-- \inst29~regout\ = DFFEAS((\inst29~regout\ & ((\inst33~regout\ & ((\inst25~4_combout\) # (!\inst31~regout\))) # (!\inst33~regout\ & ((!\inst25~4_combout\))))) # (!\inst29~regout\ & (((\inst25~4_combout\)))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "dd2a",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst29~regout\,
	datab => \inst33~regout\,
	datac => \inst31~regout\,
	datad => \inst25~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst29~regout\);

-- Location: LC_X2_Y4_N8
inst27 : maxii_lcell
-- Equation(s):
-- \inst27~regout\ = DFFEAS((\inst31~regout\ & ((\inst29~regout\ & ((\inst33~regout\) # (!\inst27~regout\))) # (!\inst29~regout\ & ((!\inst33~regout\))))) # (!\inst31~regout\ & ((\inst27~regout\ $ (\inst33~regout\)))), GLOBAL(\clock~combout\), VCC, , , , , , 
-- )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "a37c",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst31~regout\,
	datad => \inst33~regout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst27~regout\);

-- Location: PIN_A1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[3]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst27~regout\,
	oe => VCC,
	padio => ww_q(3));

-- Location: PIN_B3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[2]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst29~regout\,
	oe => VCC,
	padio => ww_q(2));

-- Location: PIN_D3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[1]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst31~regout\,
	oe => VCC,
	padio => ww_q(1));

-- Location: PIN_B1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[0]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst33~regout\,
	oe => VCC,
	padio => ww_q(0));
END structure;


