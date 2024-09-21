#!/usr/bin/env ruby

# Define the test patterns
test_patterns = ["htn", "hbtn", "hbttn", "hbtttn"]

# Get the input argument
input_arg = ARGV[0]

# Check if the input matches any of the test patterns
match_found = false
test_patterns.each do |pattern|
  if input_arg.match?(pattern)
    puts "Match found for pattern '#{pattern}'"
    match_found = true
  end
end

# If no match is found, display a message
puts "No match found" unless match_found

