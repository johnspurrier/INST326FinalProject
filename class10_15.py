from argparse import ArgumentParser
import sys

LANGUAGES = [
    # "est"
    # "eus"
    "deu"
]

ONES = ["null", "ein", "zwei", "drei", "vier", "funf", "sechs", "sieben", 
        "acht", "neun", "zehn", "elf", "zwolf", "dreizehn", "vierzehn",
        "funfzehn", "sechzen", "zeibzen", "achtzen", "neunzehn"]

TENS = ["", "zehn", "zwanzig", "dreibig", "vierzig", "funfzig", "sechzig", 
        "siebzig", "achtzig", "neunzig"]

def deu(num):
    if num == 1: 
        return "eins"
    if num < 20: 
        return ONES[num]
    if num < 100: 
        t, o = divmod(num, 10)
        if o == 0: 
            return TENS[t]
        return f"{ONES[o]}und{TENS[t]}"
    if num < 1000: 
        h, r = divmod(num, 100)
        hundreds = "hundert" if h == 1 else f"{ONES[h]}hundert"
        if r == 0: 
            return hundreds
        else: 
            return f"{hundreds}{deu(r)}"
    t, r = divmod(num, 1000)
    thousands = "tausend" if t == 1 else f"{deu(t)}tausend"
    if r == 0: 
        return thousands
    else: 
        return f"{thousands} {deu(r)}"