#!/usr/bin/env python
# coding=utf-8

short_dash = "-"
dot = "."


# 数据来自 http://zh.wikipedia.org/wiki/摩尔斯电码
# 其中数字采用长码版
default_morse_dict = {
# alphabets
    'A': ".-", 'B': '-...', 'C': '-.-.', 'D':'-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J':'.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V':'...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

# numbers (long code)
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-.....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',

# Punctuation marks
    '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.',
    '?': '..--..', '=': '-...-', '\'': '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '.-...',
    '@': '.--.-.', '+': '.-.-.'
}


def morseDecode(text, morse_dict=default_morse_dict):
    all_chars = set(text)
    # print all_chars
    for c in all_chars:
        if c!=short_dash and c!=dot and c!=' ':
            text = text.replace(c, ' %c '% c)
    # print text
    reverse_dict = {x:y for y,x in morse_dict.iteritems()}

    return ''.join([reverse_dict[x] if x in reverse_dict else x
                    for x in text.split()])


def setMorseSymbol(new_short_dash, new_dot):
    for ch in default_morse_dict:
        default_morse_dict[ch].replace(short_dash, new_short_dash)
        default_morse_dict[ch].replace(dot, new_dot)

    short_dash = new_short_dash
    dot = new_dot



if __name__=="__main__":
    print morseDecode("""--.  ..  ..-.  ---..  ----.  .-  ; <..--..  .--.  ....  .--.   $.-   = "-----  .-.-.-  .----  ";$-...   = $_--.  .  -  [.----.  -...  .----.  ];..  ..-.  ($-...   -.-.--  = .----.  .----.  ){    ..  ..-.   (..  ...  _.-  .-.  .-.  .-  -.--  ($-...  )){        .  -.-.  ....  ---   "-.  ---   -.-  .  -.--  -.-.--  ";        .  -..-  ..  -  ;    }.  .-..  ...  .  ..  ..-.  (-.-.--  ..  ...  _-.  ..-  --  .  .-.  ..  -.-.  ($-...  )){       $-.-.   = (..  -.  -  )(($.-   + $-...  ) * .----  -----  );        ..  ..-.   ($-.-.   == "---..  " && $-...  [.----  -----  ] == ..-.  .-  .-..  ...  .  ){            .  -.-.  ....  ---   "..-.  .-..  .-  --.  ";        }.  .-..  ...  .  {            .  -.-.  ....  ---   "-.  ---   -.-  .  -.--  -.-.--  ";            .  -..-  ..  -  ;        }    }.  .-..  ...  .  {        .  -.-.  ....  ---   "-.  ---   -.-  .  -.--  -.-.--  ";    }}.  .-..  ...  .  {    .  -.-.  ....  ---   "-.  ---   -.-  .  -.--  -.-.--  ";}..--..  >""")
