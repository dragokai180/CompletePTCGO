from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="64543bb2-a8ad-53af-9d2d-640bff2b8f5d",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredCharm.Name",
    display_name="Sacred Charm",
    searchable_by=["Sacred Charm", "Pokémon Tool", "SacredCharm"],
    subtypes=["Pokémon Tool"],
    collector_number=93,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Pokémon this card is attached to takes 30 less damage from attacks from your opponent's Pokémon that have an Ability (after applying Weakness and Resistance)."),
)
