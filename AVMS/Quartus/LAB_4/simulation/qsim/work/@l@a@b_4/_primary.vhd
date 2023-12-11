library verilog;
use verilog.vl_types.all;
entity LAB_4 is
    port(
        newq0           : out    vl_logic;
        b               : in     vl_logic;
        q               : out    vl_logic_vector(3 downto 0);
        clock           : in     vl_logic;
        newq1           : out    vl_logic;
        a               : in     vl_logic;
        newq2           : out    vl_logic;
        newq3           : out    vl_logic
    );
end LAB_4;
