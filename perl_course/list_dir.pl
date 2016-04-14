use strict;
use warnings;
use Path::Class;

print "Give me a DIR path fucker!";
my $path = <>;
chomp($path);
my $dir = dir($path);
while (my $file = $dir->next) {
    next if $file->is_dir();
    print $file->stringify . "\n";
}
