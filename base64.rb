if ARGV.length > 1 then
  text = ARGV[1]
else
  text = gets
end

require "base64"

flick= -> c,x { if x==1 then c.upcase else c.downcase end}


target_base64 = ""

text.scan(/..../).each do |substr|
  for i in 0..15 do
    # p substr
    s = substr.split("").each_with_index.map do |c, index|
      flick.call(substr[index], (i>>index) & 1)
    end.join('')

    p s
    bs = Base64.decode64(s)
    if bs.scan(/[[:print:]]/).join == bs then
      target_base64 << s
      break
    end
  end
end
# p target_base64

print Base64.decode64(target_base64)
