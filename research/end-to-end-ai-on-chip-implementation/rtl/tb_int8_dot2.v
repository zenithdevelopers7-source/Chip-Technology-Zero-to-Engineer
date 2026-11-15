`timescale 1ns/1ps
module tb_int8_dot2;
    reg clk = 0;
    always #5 clk = ~clk;
    reg rst_n = 0, start = 0;
    reg signed [7:0] a0 = 0, a1 = 0, b0 = 0, b1 = 0;
    wire signed [31:0] result;
    wire valid, busy;
    integer cases = 0;
    int8_dot2 dut (.clk(clk), .rst_n(rst_n), .start(start),
        .a0(a0), .a1(a1), .b0(b0), .b1(b1),
        .result(result), .valid(valid), .busy(busy));

    task run_case;
        input signed [7:0] x0, x1, y0, y1;
        input signed [31:0] expected;
        begin
            @(negedge clk);
            a0=x0; a1=x1; b0=y0; b1=y1; start=1;
            @(posedge clk); #1;
            if (!busy || valid) $fatal(1, "Expected busy during MAC");
            @(negedge clk); start=0;
            @(posedge clk); #1;
            if (!valid || busy || result !== expected)
                $fatal(1, "Wrong output. expected=%0d got=%0d valid=%b",
                       expected, result, valid);
            @(posedge clk); #1;
            if (valid) $fatal(1, "valid not a pulse");
            cases = cases + 1;
        end
    endtask

    initial begin
        $dumpfile("int8_dot2.vcd");
        $dumpvars(0, tb_int8_dot2);
        repeat (2) @(negedge clk);
        rst_n = 1;
        run_case(8'sd2, -8'sd3, 8'sd4, 8'sd5, -32'sd7);
        run_case(8'sd127, 8'sd127, 8'sd127, 8'sd127, 32'sd32258);
        run_case(-8'sd128, -8'sd128, -8'sd128, -8'sd128, 32'sd32768);
        run_case(8'sd0, 8'sd0, 8'sd5, -8'sd8, 32'sd0);
        run_case(-8'sd128, 8'sd127, 8'sd127, -8'sd128, -32'sd32512);
        run_case(8'sd1, 8'sd2, 8'sd3, 8'sd4, 32'sd11);
        $display("RTL vectors checked: %0d", cases);
        $display("All RTL tests passed!");
        $finish;
    end
endmodule
