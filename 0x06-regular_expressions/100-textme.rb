#!/usr/bin/env ruby
#  regular expression that will match a pattern

from = ARGV[0].scan(/[a-zA-Z]\d*/).flatten
to = ARGV[0].scan(/\w+/).flatten
flags = ARGV[0].scan(/\w+/).flatten

puts "#{from},#{to},#{flags}"
