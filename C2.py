# ----------------------------------------------------------------------
# C2. Degviela un braucieni
# ----------------------------------------------------------------------

# Tvertnē ir 50 litri degvielas. Viens brauciens patērē 7 litrus. Izvadi, cik braucienu var veikt un cik degvielas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Katru rezultāta rindu beidz ar punktu.


tvertne = 50
brauciens = 7
s = 0
while tvertne >= brauciens:
  s = s + 1

  tvertne = tvertne - brauciens
print("paliks pāri", tvertne , "litrs", "degvielas" )
print("Pietiks", s , "reizēm")
