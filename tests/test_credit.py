from credit import calculate_risk


def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"

# ---------- Partie B : cas limites ----------

def test_income_zero():
    assert calculate_risk(0, 500, 30) == -1


def test_income_negative():
    assert calculate_risk(-1000, 500, 30) == -1


def test_debt_zero():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3():
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6():
    assert calculate_risk(1000, 600, 30) == "MEDIUM"


# ---------- Règle ajoutée : âge minimum ----------

def test_minor_client():
    assert calculate_risk(1000, 100, 17) == -1


def test_age_exactly_18():
    assert calculate_risk(1000, 100, 18) == "LOW"    