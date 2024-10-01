def all_combinations(choices: list[list]) -> list:
    """
    :param choices:
        A list of each 'choice' - so the first entry might be all the choices for the first option
        and the second index is a list of all the choices for the second item etc.
    :return:
        A list of all the possible combinations of choices - so the first item will be choice 1 from each option,
        the second will be choice 1 from each except the 2nd choice from the last option etc.
    """
    if len(choices) == 1:
        return choices[0]

    options = []
    for c, choice in enumerate(choices):
        future_decisions = all_combinations(choices[c + 1:])
        for decision in choice:
            for future_dec in future_decisions:
                options.append([decision, future_dec])

    return options


def all_trees_from_part(part: str, required_per_minute: float, layer: int = 0) -> list:
    """
    :param part:
        The part we are finding all possible paths for
    :param required_per_minute:
        How Much the part above this one requires from this recipe per minute
    :param layer:
        What layer (how far from the top) we currently are
    :return:
    """
    # should be a list
    recipes = parts[part]
    if not recipes:
        return [[{'part': part, 'required_per_minute': required_per_minute, 'layer': layer + 1}]]

    all_ways_of_making = []

    for recipe in recipes:
        # recipe is a dict
        ways_to_make_inputs = []
        output_of_this_recipe = recipe['output_per_minute']
        ratio_required = required_per_minute / output_of_this_recipe
        # Add more info to recipe
        recipe['recipe_output_per_minute'] = output_of_this_recipe
        recipe['output_per_minute'] = output_of_this_recipe * ratio_required
        recipe['machines_required'] = ratio_required
        recipe['layer'] = layer + 1
        for recipe_input in recipe['inputs']:
            required_per_minute_from_this_input = recipe_input['required_per_minute']
            ways_to_make_this_input = all_trees_from_part(
                recipe_input['part'],
                required_per_minute_from_this_input * ratio_required,
                layer + 1
            )
            ways_to_make_inputs.append(ways_to_make_this_input)
        for way_to_make_an_input in all_combinations(ways_to_make_inputs):
            all_ways_of_making.append([recipe, way_to_make_an_input])

    return all_ways_of_making