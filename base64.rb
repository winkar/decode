if ARGV.length > 1 then
  text = ARGV[1]
else
  text = gets
end

require "base64"

flick= -> c,x { if x==1 then c.upcase else c.downcase end}


# base64_printable_set = ""

base64_printable_set = []

text.scan(/..../).each do |substr|

  base64_printable_substr = []

  flicked_substr = []

  for i in 0..15 do
    # p substr
    s = substr.split("").each_with_index.map do |c, index|
      flick.call(substr[index], (i>>index) & 1)
    end.join('')
    flicked_substr << s
  end

  flicked_substr = flicked_substr.uniq

  flicked_substr.each do |s|
    # p s
    bs = Base64.decode64(s)
    if bs.scan(/[[:print:]]/).join == bs then
      # target_base64 << s
      # break
      base64_printable_substr << s
    end
  end

  # p base64_printable_substr
  base64_printable_set << base64_printable_substr
end

# p base64_printable_set

printable_results = base64_printable_set.inject([""]) do |res_arr, s|
  res_arr.product(s).collect {|arr| arr.join}
end

# p printable_results

printable_results.each do |s|
  p Base64.decode64(s)
end
