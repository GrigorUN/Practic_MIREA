library verilog;
use verilog.vl_types.all;
entity LAB_3 is
    port(
        LESS            : out    vl_logic;
        a               : in     vl_logic_vector(2 downto 0);
        b               : in     vl_logic_vector(2 downto 0)
    );
end LAB_3;
