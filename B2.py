# ----------------------------------------------------------------------
# B2. Funkcija ar noklusējuma atlaidi
# ----------------------------------------------------------------------

# Funkcijai jāatgriež cena pēc atlaides. Noklusējuma atlaide ir 10 procenti. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Virs funkcijas pievieno komentāru # atlaide procentos.

def ar_atlaidi(cena, atlaide=10):
    # TODO: atdod cenu pēc atlaides
    return (cena-(cena*atlaide/100))
print(ar_atlaidi(200))
print(ar_atlaidi(200, 25))
