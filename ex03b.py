# regional figures for households in 1,000's
households_in_se = 3729
households_in_lon = 3569
households_in_ne = 3161
households_in_e = 2587
households_in_sco = 2509
households_in_w_mid = 2464
households_in_york_humb = 2355
households_in_e_mid = 2035
households_in_wales = 1344
households_in_ne = 1166
households_in_n_ire = 728

households_in_uk = (
households_in_se + households_in_lon +
households_in_ne + households_in_e + households_in_sco + households_in_w_mid +
households_in_york_humb + households_in_e_mid + households_in_wales + households_in_ne + households_in_n_ire
) 

households_in_england = (households_in_uk - households_in_sco - households_in_n_ire - households_in_wales)

pop_england = 56286961
pop_scotland = 5463300
pop_wales = 3152879
pop_n_ireland = 1893667

pop_uk = pop_england + pop_scotland + pop_wales + pop_n_ireland

print(f"The number of households in the UK is: {(households_in_uk*1000):,}")
print(f"The number of people in the UK is: {(pop_uk):,}")
print(f"The number of people living in each household in the uk is, on average: {(pop_uk/(households_in_uk*1000)):,.3f}")
print("\n")
print(f"The number of households in England is: {households_in_england*1000:,}")
print(f"The ratio of homes to people in the uk is: {(pop_england/(households_in_england*1000)):,.3f}.")
print("\n")
print(f"The number of households in Scotland is: {(households_in_sco*1000):,}")
print(f"The ratio of homes to people in the uk is: {(pop_scotland/(households_in_sco*1000)):,.3f}.")
print("\n")
print(f"The number of households in N Ireland is: {(households_in_n_ire*1000):,}")
print(f"The ratio of homes to people in the uk is: {(pop_n_ireland/(households_in_n_ire*1000)):,.3f}.")
print("\n")
print(f"The number of households in Wales is: {(households_in_wales*1000):,}")
print(f"The ratio of homes to people in the uk is: {(pop_wales/(households_in_wales*1000)):,.3f}.")
print("\n")