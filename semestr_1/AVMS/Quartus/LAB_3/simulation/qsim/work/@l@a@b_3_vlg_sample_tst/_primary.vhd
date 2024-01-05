library verilog;
use verilog.vl_types.all;
entity LAB_3_vlg_sample_tst is
    port(
        a               : in     vl_logic_vector(2 downto 0);
        b               : in     vl_logic_vector(2 downto 0);
        sampler_tx      : out    vl_logic
    );
end LAB_3_vlg_sample_tst;
