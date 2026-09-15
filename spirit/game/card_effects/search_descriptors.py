"""Narrow search descriptors shared by SM Trainer and Ability searches."""
import re
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.session.effects import is_pokemon_card, is_basic_pokemon, is_energy_card, is_stadium_card, is_supporter_card, is_pokemon_tool
from spirit.game.card_effects.pokemon import energy_provides_type

TYPES = "grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon|colorless"


def specific_search_predicate(text):
    text = text.casefold()
    descriptor = text.split("search your deck for ", 1)[-1].split(", reveal", 1)[0].split(".", 1)[0]
    subtypes = lambda c: {s.casefold() for s in (subtypes_for(c.archetype_id) or [])}
    name_contains = re.search(r'pokémon that (?:has|have) "([^"]+)" in (?:its|their) names?', descriptor)
    if name_contains:
        fragment = name_contains.group(1)
        return lambda c: is_pokemon_card(c) and fragment in (
            getattr(def_for(c.archetype_id), "display_name", "") or "").casefold()
    if "in any combination of supporter and stadium cards" in descriptor:
        return lambda c: is_supporter_card(c) or is_stadium_card(c)
    if "pokémon and a pokémon tool card" in descriptor:
        return lambda c: is_pokemon_card(c) or is_pokemon_tool(c)
    if "tag team cards" in descriptor:
        return lambda c: "tag team" in subtypes(c)
    if "ultra beast card" in descriptor:
        return lambda c: "ultra beast" in subtypes(c)
    if "cards named looker" in descriptor:
        return lambda c: (getattr(def_for(c.archetype_id), "display_name", "") or "").casefold() == "looker"
    if "unidentified fossil card" in descriptor:
        return lambda c: (getattr(def_for(c.archetype_id), "display_name", "") or "").casefold() == "unidentified fossil"
    # Both subtypes and elemental restrictions apply (Electromagnetic Radar).
    requested = set(re.findall(r"pokémon-(gx|ex)\b", descriptor))
    if requested and "including" not in descriptor and "isn't" not in descriptor and "except" not in descriptor:
        types = {getattr(PokemonTypes, t.upper()).value
                 for t in re.findall(rf"({TYPES}) pokémon-", descriptor)}
        # Uppercase EX and lowercase ex are distinct card classes.
        requested = {s.upper() for s in requested}
        return lambda c: is_pokemon_card(c) and bool(requested.intersection(subtypes_for(c.archetype_id) or [])) and (
            not types or bool(types.intersection(c.get_attribute(AttrID.POKEMON_TYPES) or [])))
    mixed = re.search(rf"basic ({TYPES}) pokémon or an? ({TYPES}) energy", descriptor)
    if mixed:
        pokemon_type, energy_type = (getattr(PokemonTypes, t.upper()).value for t in mixed.groups())
        return lambda c: (is_basic_pokemon(c) and pokemon_type in
                          (c.get_attribute(AttrID.POKEMON_TYPES) or [])) or (
                          is_energy_card(c) and energy_provides_type(c, energy_type))
    if "basic water pokémon or basic fighting pokémon" in descriptor:
        return lambda c: is_basic_pokemon(c) and bool(
            {PokemonTypes.WATER.value, PokemonTypes.FIGHTING.value}.intersection(
                c.get_attribute(AttrID.POKEMON_TYPES) or []))
    if "stadium card" in descriptor and "search your deck for" in text:
        return is_stadium_card
    return None
