library verilog;
use verilog.vl_types.all;
entity LAB_4_vlg_check_tst is
    port(
        newq0           : in     vl_logic;
        newq1           : in     vl_logic;
        newq2           : in     vl_logic;
        newq3           : in     vl_logic;
        q               : in     vl_logic_vector(3 downto 0);
        sampler_rx      : in     vl_logic
    );
end LAB_4_vlg_check_tst;
