
# Dictionary with season and its advice
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "spring": "Apply a light layer of mulch to help retain moisture,"
    " keep the soil cool, and prevent weeds.\n",
    "autumn": "Water in the mornings to allow plants to absorb"
    " moisture before the heat of the day.\n",
}

# Dictionary with plant_type and its advice
plant_type = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "tree": "Consider planting trees and shrubs in September"
    " for autumn blooms.",
    "herbs": "Consider planting sprouted garlic bulbs"
    "from the kitchen for their flavorful leaves.",
}


def get_advice(season, plant):
    """
    Determine which advice to give based on season and plant.

    Args:
        season: name of season.
        plant: Type of plant to advise on.

    Returns:
        String: advice on season and plant.
    """

    # Variable to hold gardening advice
    advice = ""

    # Determine advice based on the season
    if season in season_advice:
        advice += f"\nAdvice for season: {season.title()} \n"
        for info in season_advice[season]:
            advice += f"{info}"
    else:
        advice += (
            "\n That season is not available, try (Autumn, Summer,"
            " Winter, Spring)"
        )

    # Determine advice based on the plant type
    if plant in plant_type:
        advice += f"\nAdvice for plant_type: {plant.title()} \n"
        for info in plant_type[plant]:
            advice += f"{info}"
    else:
        advice += (
            "\n That season is not available, try (Tree, Flower,"
            "Herbs, Vegetable)"
        )

    # Print the generated advice
    return advice


# Allow user to enter season and plant type
season = input("Enter the season you're in: ")
plant = input("What plant type do you want advice on? ")

# Print the season advice with the plant type
print(get_advice(season, plant))
