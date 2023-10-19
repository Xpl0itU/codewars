def open_or_senior(data):
    results = []
    for age, handicap in data:
        if age >= 55:
            if handicap > 7:
                results.append("Senior")
                continue
        results.append("Open")
    return results