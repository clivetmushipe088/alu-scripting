#!/usr/bin/env ruby
# my_script.rb

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide an argument."
else
  # Print the provided argument
  puts "You entered: #{ARGV[0]}"
end

