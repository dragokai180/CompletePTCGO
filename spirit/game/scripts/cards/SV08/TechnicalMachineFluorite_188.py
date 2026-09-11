from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="924a1ac5-f41e-583b-a51a-c95a04675ed3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineFluorite.Name",
    display_name="Technical Machine: Fluorite",
    searchable_by=["Technical Machine: Fluorite", "Pokémon Tool", "TechnicalMachineFluorite"],
    subtypes=["Pokémon Tool"],
    collector_number=188,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn."),
    granted_abilities=[
        Attack(
            title="Fluorite",
            game_text="Discard all Energy from this Pokémon, and heal all damage from each of your Tera Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
