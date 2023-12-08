library verilog;
use verilog.vl_types.all;
entity LAB_4_vlg_sample_tst is
    port(
        a               : in     vl_logic;
        b               : in     vl_logic;
        clock           : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end LAB_4_vlg_sample_tst;
