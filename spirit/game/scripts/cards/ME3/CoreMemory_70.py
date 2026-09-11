from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="3794b576-c318-558c-9dbf-56a2153b0179",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoreMemory.Name",
    display_name="Core Memory",
    searchable_by=["Core Memory", "Pokémon Tool", "CoreMemory"],
    subtypes=["Pokémon Tool"],
    collector_number=70,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Mega Zygarde ex this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.)"),
    granted_abilities=[
        Attack(
            title="Geobuster",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=350,
            effect=standard_attack,
        ),
    ],
)
