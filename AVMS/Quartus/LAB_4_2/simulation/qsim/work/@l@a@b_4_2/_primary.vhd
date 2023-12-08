library verilog;
use verilog.vl_types.all;
entity LAB_4_2 is
    port(
        a               : in     vl_logic;
        b               : in     vl_logic;
        clock           : in     vl_logic;
        q               : out    vl_logic_vector(3 downto 0)
    );
end LAB_4_2;
