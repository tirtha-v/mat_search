

## Overview
The package searches for materials given the properties of the materials from the Materials Project platform. It requires an API key to access the Materials Project Database. The package allows users to specify various properties of the materials to search for.

## Usage
To use the package, users need to provide the following inputs:

1. **API Key**: The API key is required to access the Materials Project Database.
2. **Property**: Users can specify the property they want to search for. The available properties and their descriptions are listed below:
    - `band_gap` (Tuple[float, float]): Minimum and maximum band gap in eV to consider.
    - `density` (Tuple[float, float]): Minimum and maximum density to consider.
    - `e_electronic` (Tuple[float, float]): Minimum and maximum electronic dielectric constant to consider.
    - `e_ionic` (Tuple[float, float]): Minimum and maximum ionic dielectric constant to consider.
    - `e_total` (Tuple[float, float]): Minimum and maximum total dielectric constant to consider.
    - `efermi` (Tuple[float, float]): Minimum and maximum fermi energy in eV to consider.
    - `elastic_anisotropy` (Tuple[float, float]): Minimum and maximum value to consider for the elastic anisotropy.
    - `energy_above_hull` (Tuple[float, float]): Minimum and maximum energy above the hull in eV/atom to consider.
    - `equilibrium_reaction_energy` (Tuple[float, float]): Minimum and maximum equilibrium reaction energy in eV/atom to consider.
    - `formation_energy` (Tuple[float, float]): Minimum and maximum formation energy in eV/atom to consider.
    - `g_reuss` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Reuss average of the shear modulus.
    - `g_voigt` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Voigt average of the shear modulus.
    - `g_vrh` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Voigt-Reuss-Hill average of the shear modulus.
    - `k_reuss` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Reuss average of the bulk modulus.
    - `k_voigt` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Voigt average of the bulk modulus.
    - `k_vrh` (Tuple[float, float]): Minimum and maximum value in GPa to consider for the Voigt-Reuss-Hill average of the bulk modulus.
    - `n` (Tuple[float, float]): Minimum and maximum refractive index to consider.
    - `piezoelectric_modulus` (Tuple[float, float]): Minimum and maximum piezoelectric modulus to consider.
    - `poisson_ratio` (Tuple[float, float]): Minimum and maximum value to consider for Poisson's ratio.
    - `shape_factor` (Tuple[float, float]): Minimum and maximum shape factor values to consider.
    - `surface_energy_anisotropy` (Tuple[float, float]): Minimum and maximum surface energy anisotropy values to consider.
    - `total_energy` (Tuple[float, float]): Minimum and maximum corrected total energy in eV/atom to consider.
    - `total_magnetization` (Tuple[float, float]): Minimum and maximum total magnetization values to consider.
    - `total_magnetization_normalized_formula_units` (Tuple[float, float]): Minimum and maximum total magnetization values normalized by formula units to consider.
    - `total_magnetization_normalized_vol` (Tuple[float, float]): Minimum and maximum total magnetization values normalized by volume to consider.
    - `uncorrected_energy` (Tuple[float, float]): Minimum and maximum uncorrected total energy in eV/atom to consider.
    - `volume` (Tuple[float, float]): Minimum and maximum volume to consider.
    - `weighted_surface_energy` (Tuple[float, float]): Minimum and maximum weighted surface energy in J/m² to consider.
    - `weighted_work_function` (Tuple[float, float]): Minimum and maximum weighted work function in eV to consider.

3. **Min and Max Values of Property**: Users need to specify the minimum and maximum values of the property they are searching for.

4. **Number of Materials Needed**: Finally, users need to specify the number of materials they want as output.


