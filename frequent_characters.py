frequency = dict()
text = "In physics, a redshift is an increase in the wavelength, or equivalently, a decrease in the frequency and photon energy, of electromagnetic radiation (such as light). The opposite change, a decrease in wavelength and increase in frequency and energy, is known as a blueshift. The terms derive from the colours red and blue, which form the extremes of the visible-light spectrum. Three forms of redshift occur in astronomy and cosmology: Doppler redshifts due to the relative motions of radiation sources, gravitational redshift as radiation escapes from gravitational potentials, and cosmological redshifts caused by the universe expanding. Automated astronomical redshift surveys are an important tool for learning about the large scale structure of the universe. Examples of strong redshifting are a gamma ray perceived as an X-ray, or initially visible light perceived as radio waves. The initial heat from the Big Bang has redshifted far down to become the cosmic microwave background"

for ch in text:
    if frequency.get(ch)==None:
        frequency[ch] ="*"
    else:
        frequency[ch] += "*"    

for ch in frequency:
    print(ch,": ", frequency[ch])
