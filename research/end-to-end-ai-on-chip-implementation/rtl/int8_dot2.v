// Educational two-element signed INT8 dot product.
// Handshake: pulse start while idle. valid pulses for 1 cycle when result is ready.
// The second product is accumulated on the following rising clock edge.
module int8_dot2 (
    input  wire               clk,
    input  wire               rst_n,
    input  wire               start,
    input  wire signed [7:0]  a0,
    input  wire signed [7:0]  a1,
    input  wire signed [7:0]  b0,
    input  wire signed [7:0]  b1,
    output reg  signed [31:0] result,
    output reg                valid,
    output wire               busy
);
    reg active;
    reg signed [7:0] ra1, rb1;
    reg signed [31:0] accumulator;
    wire signed [15:0] first_product = a0 * b0;
    wire signed [15:0] second_product = ra1 * rb1;

    assign busy = active;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            active      <= 1'b0;
            ra1         <= 8'sd0;
            rb1         <= 8'sd0;
            accumulator <= 32'sd0;
            result      <= 32'sd0;
            valid       <= 1'b0;
        end else begin
            valid <= 1'b0;
            if (!active) begin
                if (start) begin
                    accumulator <= {{16{first_product[15]}}, first_product};
                    ra1         <= a1;
                    rb1         <= b1;
                    active      <= 1'b1;
                end
            end else begin
                result <= accumulator + {{16{second_product[15]}}, second_product};
                active <= 1'b0;
                valid  <= 1'b1;
            end
        end
    end
endmodule
