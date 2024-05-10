infrastructure_systems = {
    "energy": ["power"],
    "transportation": ["roads", "airports", "railways"],
    "water": ["water_supply"],
    "waste": ["waste_solid", "waste_water"],
    "telecommunication": ["telecom"],
    "healthcare": ["health"],
    "education": ["education_facilities"],
}

weight_assets = {
    "energy": {
        "power": {
            "line_km": 1 / 7,
            "minor_line_km": 1 / 7,
            "cable_km": 1 / 7,
            "plant_km2": 1 / 7,
            "substation_km2": 1 / 7,
            "power_tower_count": 1 / 7,
            "power_pole_count": 1 / 7,
        }
    },
    "transportation": {
        "roads": {"primary_km": 1 / 3, "secondary_km": 1 / 3, "tertiary_km": 1 / 3},
        "airports": {"airports_km2": 1},
        "railways": {"railway_km": 1},
    },
    "ports": {"industrial_km2": 1 / 3, "harbour_km2": 1 / 3, "port_km2": 1 / 3},
    "water": {
        "water_supply": {
            "water_tower_km2": 1 / 5,
            "water_well_km2": 1 / 5,
            "reservoir_covered_km2": 1 / 5,
            "water_works_km2": 1 / 5,
            "reservoir_km2": 1 / 5,
        }
    },
    "waste": {
        "waste_solid": {"landfill_km2": 1 / 2, "waste_transfer_station_km2": 1 / 2},
        "waste_water": {"wastewater_treatment_plant_km2": 1},
    },
    "telecommunication": {
        "telecom": {"communication_tower_count": 1 / 2, "mast_count": 1 / 2}
    },
    "healthcare": {
        "health": {
            "clinic_count": 1 / 12,
            "doctors_count": 1 / 12,
            "hospital_count": 1 / 12,
            "dentist_count": 1 / 12,
            "pharmacy_count": 1 / 12,
            "physiotherapist_count": 1 / 12,
            "alternative_count": 1 / 12,
            "laboratory_count": 1 / 12,
            "optometrist_count": 1 / 12,
            "rehabilitation_count": 1 / 12,
            "blood_donation_count": 1 / 12,
            "birthing_center_count": 1 / 12,
        }
    },
    "education": {
        "education_facilities": {
            "college_km2": 1 / 5,
            "kindergarten_km2": 1 / 5,
            "library_km2": 1 / 5,
            "school_km2": 1 / 5,
            "university_km2": 1 / 5,
        }
    },
}
