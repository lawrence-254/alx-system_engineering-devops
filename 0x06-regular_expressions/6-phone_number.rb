#!/usr/bin/env ruby
#  regular expression that will match a pattern

puts ARGV[0].scan(/^\d{10,10}$/).join
