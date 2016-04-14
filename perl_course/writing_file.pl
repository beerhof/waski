use strict;
use warnings;
use Path::Class;
use autodie;

&writing;   #func. declaration
sub writing{    #func. open.

    my $dir = dir("/tmp");
    my $file = $dir -> file("file.txt");
    my $file_handle = $file -> openw();
    my @list_of_strings_to_add = ("fuck", "dupa", 123, "six", "six", "six", 666);

    foreach my $line (@list_of_strings_to_add) {
        $file_handle ->print ($line."\n");
    }
}   #func. close
