use warnings;
use strict;

&my_func;
sub my_func{
    for (
        my $loop=1; $loop<=10; $loop++
        )
        {
            print"Hello\n";
        }

    #foreach
    foreach my $loop (0..9) {
        print "$loop\n"}

    foreach my $loop (0..9) {
        print "Hello\n";
        }
}
