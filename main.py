import astropy.units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time

obs = EarthLocation(lat = 43 * u.deg + 79 * u.arcmin + 48 * u.arcsec, lon = -79 * u.deg + 34 * u.arcmin + 82 * u.arcsec)
# e.g. 43.7948, -79.3482

time_shift = -4 * u.hour
# e.g. print(Time.now() + time_shift)

print(dir(astropy.time))


