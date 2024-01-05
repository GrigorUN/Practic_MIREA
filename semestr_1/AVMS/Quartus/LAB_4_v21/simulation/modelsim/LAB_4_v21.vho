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

-- DATE "12/18/2023 15:14:35"

-- 
-- Device: Altera EPM240T100C3 Package TQFP100
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY IEEE;
LIBRARY MAXII;
USE IEEE.STD_LOGIC_1164.ALL;
USE MAXII.MAXII_COMPONENTS.ALL;

ENTITY 	LAB_4_v21 IS
    PORT (
	q : OUT std_logic_vector(3 DOWNTO 0);
	clock : IN std_logic;
	b : IN std_logic;
	a : IN std_logic
	);
END LAB_4_v21;

-- Design Ports Information
-- q[3]	=>  Location: PIN_64,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[2]	=>  Location: PIN_67,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[1]	=>  Location: PIN_66,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[0]	=>  Location: PIN_68,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- b	=>  Location: PIN_69,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- clock	=>  Location: PIN_14,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- a	=>  Location: PIN_72,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default


ARCHITECTURE structure OF LAB_4_v21 IS
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
SIGNAL \inst~1_combout\ : std_logic;
SIGNAL \a~combout\ : std_logic;
SIGNAL \inst~0_combout\ : std_logic;
SIGNAL \inst8~0_combout\ : std_logic;
SIGNAL \inst23~0_combout\ : std_logic;
SIGNAL \inst28~regout\ : std_logic;
SIGNAL \inst~2_combout\ : std_logic;
SIGNAL \inst24~2_combout\ : std_logic;
SIGNAL \inst10~2_combout\ : std_logic;
SIGNAL \inst10~4_combout\ : std_logic;
SIGNAL \inst29~regout\ : std_logic;
SIGNAL \inst24~4_combout\ : std_logic;
SIGNAL \inst24~3_combout\ : std_logic;
SIGNAL \inst27~regout\ : std_logic;
SIGNAL \inst25~4_combout\ : std_logic;
SIGNAL \inst26~regout\ : std_logic;

BEGIN

q <= ww_q;
ww_clock <= clock;
ww_b <= b;
ww_a <= a;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: PIN_14,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\clock~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_clock,
	combout => \clock~combout\);

-- Location: PIN_69,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\b~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_b,
	combout => \b~combout\);

-- Location: LC_X7_Y3_N8
\inst~1\ : maxii_lcell
-- Equation(s):
-- \inst~1_combout\ = (\inst27~regout\ & (!\inst26~regout\ & (!\inst29~regout\ & \inst28~regout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0200",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \inst26~regout\,
	datac => \inst29~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst~1_combout\);

-- Location: PIN_72,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\a~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_a,
	combout => \a~combout\);

-- Location: LC_X7_Y3_N9
\inst~0\ : maxii_lcell
-- Equation(s):
-- \inst~0_combout\ = (\inst27~regout\ & (\inst26~regout\ & (!\inst28~regout\ & !\inst29~regout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0008",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \inst26~regout\,
	datac => \inst28~regout\,
	datad => \inst29~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst~0_combout\);

-- Location: LC_X7_Y3_N5
\inst8~0\ : maxii_lcell
-- Equation(s):
-- \inst8~0_combout\ = ((\a~combout\ & ((\inst~0_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "cc00",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	datab => \a~combout\,
	datad => \inst~0_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst8~0_combout\);

-- Location: LC_X6_Y3_N5
\inst23~0\ : maxii_lcell
-- Equation(s):
-- \inst23~0_combout\ = (\inst28~regout\ & (!\inst26~regout\ & ((!\inst27~regout\) # (!\inst29~regout\)))) # (!\inst28~regout\ & ((\inst27~regout\ & ((\inst26~regout\))) # (!\inst27~regout\ & (\inst29~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0e72",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst28~regout\,
	datad => \inst26~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~0_combout\);

-- Location: LC_X7_Y3_N2
inst28 : maxii_lcell
-- Equation(s):
-- \inst28~regout\ = DFFEAS((\inst8~0_combout\) # (((\inst~1_combout\ & \b~combout\)) # (!\inst23~0_combout\)), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "f8ff",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst~1_combout\,
	datab => \b~combout\,
	datac => \inst8~0_combout\,
	datad => \inst23~0_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst28~regout\);

-- Location: LC_X7_Y3_N0
\inst~2\ : maxii_lcell
-- Equation(s):
-- \inst~2_combout\ = (!\inst27~regout\ & (!\inst26~regout\ & (\inst29~regout\ & \inst28~regout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1000",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \inst26~regout\,
	datac => \inst29~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst~2_combout\);

-- Location: LC_X7_Y3_N7
\inst24~2\ : maxii_lcell
-- Equation(s):
-- \inst24~2_combout\ = (\b~combout\ & (((\inst~2_combout\) # (\inst~1_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "aaa0",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datac => \inst~2_combout\,
	datad => \inst~1_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~2_combout\);

-- Location: LC_X6_Y3_N9
\inst10~2\ : maxii_lcell
-- Equation(s):
-- \inst10~2_combout\ = ((!\inst27~regout\ & (\inst29~regout\ & \inst26~regout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "3000",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	datab => \inst27~regout\,
	datac => \inst29~regout\,
	datad => \inst26~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst10~2_combout\);

-- Location: LC_X6_Y3_N7
\inst10~4\ : maxii_lcell
-- Equation(s):
-- \inst10~4_combout\ = (\inst27~regout\ & (!\inst28~regout\ & (\inst29~regout\ $ (\inst26~regout\)))) # (!\inst27~regout\ & (((!\inst29~regout\ & !\inst26~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0225",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst27~regout\,
	datab => \inst28~regout\,
	datac => \inst29~regout\,
	datad => \inst26~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst10~4_combout\);

-- Location: LC_X7_Y3_N6
inst29 : maxii_lcell
-- Equation(s):
-- \inst29~regout\ = DFFEAS(((\inst24~2_combout\) # ((\inst10~2_combout\) # (\inst10~4_combout\))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "fffc",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	datab => \inst24~2_combout\,
	datac => \inst10~2_combout\,
	datad => \inst10~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst29~regout\);

-- Location: LC_X6_Y3_N6
\inst24~4\ : maxii_lcell
-- Equation(s):
-- \inst24~4_combout\ = (\inst26~regout\ & ((\inst27~regout\ & (\inst29~regout\)) # (!\inst27~regout\ & ((\inst28~regout\))))) # (!\inst26~regout\ & ((\inst29~regout\) # ((!\inst28~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "b8af",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst28~regout\,
	datad => \inst26~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~4_combout\);

-- Location: LC_X7_Y3_N3
\inst24~3\ : maxii_lcell
-- Equation(s):
-- \inst24~3_combout\ = ((\inst24~2_combout\) # ((!\a~combout\ & \inst~0_combout\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "f3f0",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	datab => \a~combout\,
	datac => \inst24~2_combout\,
	datad => \inst~0_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~3_combout\);

-- Location: LC_X7_Y3_N4
inst27 : maxii_lcell
-- Equation(s):
-- \inst27~regout\ = DFFEAS((\inst24~4_combout\ & (((\inst24~3_combout\) # (!\inst28~regout\)) # (!\inst29~regout\))) # (!\inst24~4_combout\ & (\inst24~3_combout\ & ((!\inst28~regout\) # (!\inst29~regout\)))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "f770",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst29~regout\,
	datab => \inst28~regout\,
	datac => \inst24~4_combout\,
	datad => \inst24~3_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst27~regout\);

-- Location: LC_X6_Y3_N2
\inst25~4\ : maxii_lcell
-- Equation(s):
-- \inst25~4_combout\ = (\inst28~regout\ & ((\inst29~regout\) # ((!\b~combout\ & !\inst26~regout\)))) # (!\inst28~regout\ & ((\inst29~regout\ $ (\inst26~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "c3f4",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datab => \inst28~regout\,
	datac => \inst29~regout\,
	datad => \inst26~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst25~4_combout\);

-- Location: LC_X7_Y3_N1
inst26 : maxii_lcell
-- Equation(s):
-- \inst26~regout\ = DFFEAS((\inst27~regout\ & (((\inst25~4_combout\)))) # (!\inst27~regout\ & (((!\inst28~regout\ & \inst25~4_combout\)) # (!\inst29~regout\))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "bf05",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst27~regout\,
	datab => \inst28~regout\,
	datac => \inst29~regout\,
	datad => \inst25~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst26~regout\);

-- Location: PIN_64,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[3]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst26~regout\,
	oe => VCC,
	padio => ww_q(3));

-- Location: PIN_67,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[2]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst27~regout\,
	oe => VCC,
	padio => ww_q(2));

-- Location: PIN_66,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[1]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst28~regout\,
	oe => VCC,
	padio => ww_q(1));

-- Location: PIN_68,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[0]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst29~regout\,
	oe => VCC,
	padio => ww_q(0));
END structure;


