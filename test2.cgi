#!/usr/bin/perl -w
use lib "..";
use lib "../..";
require "common.cgi";

use strict;
use CGI qw(:standard);
use DBI;
use Time::Local;

my $dbh = dbConnect();

print "\n";

for my $i (0..7)
{
	print int(rand(8))+1;
	print "\n";
}


1;