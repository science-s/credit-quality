def calculate_risk(income, debt, age):
    """Évalue le risque de crédit d'un client.

    Retourne "HIGH", "MEDIUM" ou "LOW" selon le ratio dette / revenu,
    ou -1 si les données sont invalides (revenu <= 0 ou client mineur).
    """
    if income <= 0 or age < 18:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"