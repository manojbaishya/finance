def compound_interest(principal, roi_annual, freq_per_year, time):
    return principal * ((1 + roi_annual / freq_per_year) ** (time * freq_per_year))
