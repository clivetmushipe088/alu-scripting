#!/usr/bin/env ruby

# Check if an argument is passed
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

# Assign the argument to a variable
input_string = ARGV[0]

# Regular expression to match the desired pattern
pattern = /^hbt+n$/

# Check if the input matches the pattern
if input_string.match(pattern)
  puts input_string
else
  puts "No match"
end
