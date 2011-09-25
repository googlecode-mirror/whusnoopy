#!/usr/bin/perl -w
## Copyright (c) 2011 by whusnoopy

use strict;

if (@ARGV < 1) {
    die "Not enough arguments\n";
}

my $input_filename = $ARGV[0];

if (! open IN, $input_filename) {
    die "Can not open input file [$input_filename]\n";
}

my $outfile = $input_filename;
$outfile =~ s/$/.out/;

if (! open OUT, "> $outfile") {
    die "Can not open output file [$outfile]\n";
}

while (<IN>) {
    my $input = $_;
    my @parts = split /fred/i, $input;
    foreach my $p (@parts) {
        $p =~ s/wilma/fred/i;
    }
    my $output = join "wilma", @parts;
    print OUT $output;
}
