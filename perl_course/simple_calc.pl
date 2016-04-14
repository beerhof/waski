use strict;
use warnings;


&sum;
sub sum{
my $first = "type some INT";
my $first_ans = <>;

my $sec = "type another INT";
my $sec_ans = <>;
my $answer = $first_ans + $sec_ans;
print "sum of your INTs = ".$answer. "\n";
}

