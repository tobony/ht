# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from __future__ import division
from math import exp
import numpy as np
from scipy.constants import sigma, h, c, k, pi
import os
from io import open

__all__ = ['blackbody_spectral_radiance', 'q_rad', 'solar_spectrum']

folder = os.path.join(os.path.dirname(__file__), 'data')

def blackbody_spectral_radiance(T, wavelength):
    r'''Returns the spectral radiance, in units of W/m^2/sr/µm.

    .. math::
        I_{\lambda,blackbody,e}(\lambda,T)=\frac{2hc_o^2}
        {\lambda^5[\exp(hc_o/\lambda k T)-1]}

    Parameters
    ----------
    T : float
        Temperature of the surface, [K]
    wavelength : float
        Length of the wave to be considered, [m]

    Returns
    -------
    I : float
        Spectral radiance [W/m^2/sr/µm]

    Notes
    -----
    Can be used to derive the Stefan-Boltzman law, or determine the maximum
    radiant frequency for a given temperature.

    Examples
    --------
    Checked with Spectral-calc.com, at [2]_.

    >>> blackbody_spectral_radiance(800., 4E-6)
    1311692056.2430143

    References
    ----------
    .. [1] Bergman, Theodore L., Adrienne S. Lavine, Frank P. Incropera, and
       David P. DeWitt. Introduction to Heat Transfer. 6E. Hoboken, NJ:
       Wiley, 2011.
    .. [2] Spectral-calc.com. Blackbody Calculator, 2015.
       http://www.spectralcalc.com/blackbody_calculator/blackbody.php
    '''
    return 2.*h*c**2/wavelength**5/(exp(h*c/(wavelength*T*k)) - 1.)


def q_rad(emissivity, T, T2=0):
    r'''Returns the radiant heat flux of a surface, optionally including
    assuming radiant heat transfer back to the surface.

    .. math::
        q = \epsilon \sigma (T_1^4 - T_2^4)

    Parameters
    ----------
    emissivity : float
        Fraction of black-body radiation which is emitted, [-]
    T : float
        Temperature of the surface, [K]
    T2 : float, optional
        Temperature of the surrounding material of the surface [K]

    Returns
    -------
    q : float
        Heat exchange [W/m^2]

    Notes
    -----
    Emissivity must be less than 1. T2 may be larger than T.

    Examples
    --------
    >>> q_rad(emissivity=1, T=400)
    1451.613952

    >>> q_rad(.85, T=400, T2=305.)
    816.7821722650002

    References
    ----------
    .. [1] Bergman, Theodore L., Adrienne S. Lavine, Frank P. Incropera, and
       David P. DeWitt. Introduction to Heat Transfer. 6E. Hoboken, NJ:
       Wiley, 2011.
    '''
    return sigma*emissivity*(T**4 - T2**4)


def solar_spectrum(model='SOLAR-ISS'):
    r'''Returns the solar spectrum of the sun according to the specified model.
    Only the 'SOLAR-ISS' model is supported.

    Parameters
    ----------
    model : str, optional
        The model to use; 'SOLAR-ISS' is the only model available, [-]

    Returns
    -------
    wavelengths : ndarray
        The wavelengths of the solar spectra, [m]
    SSI : ndarray
        The solar spectral irradiance of the sun, [W/(m^2*m)]
    uncertainties : ndarray
        The estimated absolute uncertainty of the measured spectral irradiance  
        of the sun, [W/(m^2*m)]

    Notes
    -----
    The power of the sun changes as the earth gets closer or further away.
    
    In [1]_, the UV and VIS data come from observations in 2008; the IR comes
    from measurements made from 2010-2016. There is a further 28 W/m^2 for the
    3 micrometer to 160 micrometer range, not included in this model. All data
    was corrected to a standard distance of one astronomical unit from the Sun,
    as is the resultant spectrum. 
    
    The variation of the spectrum as a function of distance from the sun should
    alter only the absolute magnitudes.
    
    [2]_ contains another dataset.
    
    Examples
    --------
    >>> wavelengths, SSI, uncertainties = solar_spectrum()
    
    Calculate the minimum and maximum values of the wavelengths (0.5 nm/3000nm)
    and SSI:
        
    >>> min(wavelengths), max(wavelengths), min(SSI), max(SSI)
    (5.0000000000000003e-10, 2.9999000000000003e-06, 1330.0, 2256817820.0)
    
    Integration - calculate the solar constant, in untis of W/m^2 hitting
    earth's atmosphere.
    
    >>> np.trapz(SSI, wavelengths)
    1344.8029782379999

    References
    ----------
    .. [1] Meftah, M., L. Damé, D. Bolsée, A. Hauchecorne, N. Pereira, D. 
       Sluse, G. Cessateur, et al. "SOLAR-ISS: A New Reference Spectrum Based 
       on SOLAR/SOLSPEC Observations." Astronomy & Astrophysics 611 (March 1, 
       2018): A1. https://doi.org/10.1051/0004-6361/201731316.
    .. [2] Woods Thomas N., Chamberlin Phillip C., Harder Jerald W., Hock 
       Rachel A., Snow Martin, Eparvier Francis G., Fontenla Juan, McClintock
       William E., and Richard Erik C. "Solar Irradiance Reference Spectra 
       (SIRS) for the 2008 Whole Heliosphere Interval (WHI)." Geophysical
       Research Letters 36, no. 1 (January 1, 2009).
       https://doi.org/10.1029/2008GL036373.
    '''
    if model == 'SOLAR-ISS':
        pth = os.path.join(folder, 'solar_iss_2018_spectrum.dat')
        data = np.loadtxt(pth)
        wavelengths, SSI, uncertainties = data[:, 0], data[:, 1], data[:, 2]
        
        wavelengths = wavelengths*1E-9
        SSI = SSI*1E9
        
        # Convert -1 uncertainties to nans
        uncertainties[uncertainties == -1] = np.nan
        
        uncertainties = uncertainties*1E9
    return wavelengths, SSI, uncertainties

