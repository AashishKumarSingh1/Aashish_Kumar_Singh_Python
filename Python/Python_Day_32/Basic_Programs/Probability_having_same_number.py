from fractions import Fraction
choices={1,2,3,4,5,6}
total_outcome=pow(len(choices),2)
favourable_outcome=len(choices)
fraction_result = Fraction(favourable_outcome, total_outcome)
print(fraction_result)