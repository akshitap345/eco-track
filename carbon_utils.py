def estimate_carbon(km, kwh):
    """
    Estimate CO₂ footprint based on:
    - Transport: 0.12 kg CO₂ per km
    - Electricity: 0.5 kg CO₂ per kWh
    """
    return round(km * 0.12 + kwh * 0.5, 2)
def calculate_transport_emissions(km, mode):
    factors = {'car': 0.21, 'bus': 0.11, 'train': 0.05, 'bike': 0.0, 'walk': 0.0}
    return km * factors.get(mode, 0.0)

def calculate_energy_emissions(kwh):
    return kwh * 0.43  # average CO2 per kWh in kg

def total_carbon_footprint(data):
    transport = calculate_transport_emissions(data['km'], data['mode'])
    energy = calculate_energy_emissions(data['kwh'])
    return round(transport + energy, 2)