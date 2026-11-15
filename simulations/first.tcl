# First NS-2 test program

set ns [new Simulator]

puts "NS-2 Simulator Started Successfully"

$ns at 1.0 "puts {Simulation is running}"
$ns at 2.0 "finish"

proc finish {} {
    puts "Simulation Completed Successfully"
    exit 0
}

$ns run
