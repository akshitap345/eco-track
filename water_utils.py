def estimate_water_usage(showers, laundry, dishes):
    """
    Estimate water usage in liters based on:
    - showers (liters per shower = 50)
    - laundry (liters per load = 70)
    - dishes (liters per run = 15)
    """
    return (showers * 50) + (laundry * 70) + (dishes * 15)
def estimate_daily_water_usage(shower_min, laundry_count, dish_count):
    shower = shower_min * 9  # liters per min
    laundry = laundry_count * 70
    dishes = dish_count * 15
    return round(shower + laundry + dishes, 2)