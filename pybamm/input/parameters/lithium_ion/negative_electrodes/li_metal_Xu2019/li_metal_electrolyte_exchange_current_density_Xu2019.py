from pybamm import constants, Parameter


def li_metal_electrolyte_exchange_current_density_Xu2019(c_e, c_s_surf, T):
    """
    Exchange-current density for Butler-Volmer reactions between li metal and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Xu, Shanshan, Chen, Kuan-Hung, Dasgupta, Neil P., Siegel, Jason B. and
    Stefanopoulou, Anna G. "Evolution of Dead Lithium Growth in Lithium Metal Batteries:
    Experimentally Validated Model of the Apparent Capacity Loss." Journal of The
    Electrochemical Society 166.14 (2019): A3456-A3463.

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 3.5e-8 * constants.F  # (A/m2)(mol/m3) - includes ref concentrations
    c_Li = Parameter("Lithium metal concentration [mol.m-3]")

    return m_ref * c_Li ** 0.5 * c_e ** 0.5
