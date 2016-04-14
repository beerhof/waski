use strict; #to zawsze musi byc, dlatego ze wymaga deklaracji zmiennych przez MY
use warnings; #warningi po uruchomieniu
use Path::Class; #sciezki do plikow, katalogow itp
use autodie; #dzieki temu nie trzeba tak jakby zamykac operacji, cos jak open(plik) close(plik) w pythonie
use Time::HiRes; #sleepy :D

&ask_save;                             # & tym znaczkiem deklarujesz funkcje
sub ask_save{                          # sub nazwa_funkcji { tak otwiera sie blok funkcji
    
    my $question = "Please type something fucker!\n";   # my $jakas_zmienna -tak uzywasz zmiennej pierwszy raz, przez my
    print $question;            #no wiadomo
    my $answer = <>;            # <> to jest input z klawiatury
    chomp($answer);             # chomp usuwa entery przy inputach

    print "Your text: $answer\n";
    print "Do you want to save it? yes/no >>> ";

    my $save = <>;
    chomp($save);

    my $yes = "yes";
    my $no = "no";

    if ($save eq $yes){                           #blok ifowy-elifowo-elsowy
        print "OK! i wll save it for you\n";
        Time::HiRes::sleep(0.5);                  #to jest sleep pol sekundy
        print "Give me the path then>>> ";
        my $path = <>;
        chomp($path);
        my $dir = dir($path);                    #tak wskazujesz katalog, $path jak widac wyzej, jest podawane z klawiatury
        print "Enter name of this file >>> ";
        my $filename = <>;
        chomp($filename);
        my $file = $dir -> file($filename);     #to jest otwarcie pliku     
        my $fh = $file -> openw();              #w perlu zeby cokolwiek otworzyc musi byc podane takie cos jak HANDLER, to jest cos w stylu referencji
        $fh -> print ($answer."\n");            #na logike - handler pliku wyzej, printuje cos, co jest przypisane wyzej do zmiennej $answer do pliku . (kropka) w perlu to cos jak przecinek lub + (plus) w pythonie
        print "Saved\n";
        Time::HiRes::sleep(0.5);
    }                                           #zamyka ifa

    elsif($save eq $no){                        #pythonowy odpowiednik ELIF, tak samo sie pisze jak ifa i elsa
        print "Text will not be saved!\n";
    }                                           #zamyka elifa

    else{
        print "Invalid Keyboard Input!\n";
    }                                           #zamyka elsa
}                                               #zamyka cala funkcje

#w perlu kazda instrukcje (wciecia i linijki nie maja znaczenia), konczy sie srednikiem :) 
