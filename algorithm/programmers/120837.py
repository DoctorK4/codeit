big = 5
small = 3
xs = 1

def solution(hp):
    big_unit = hp // big
    small_unit = (hp - (big * big_unit)) // small
    xs_unit = (hp - (big * big_unit) - (small * small_unit)) // xs
    return big_unit + small_unit + xs_unit