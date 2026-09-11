from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="cf046c56-f477-5310-a447-b823ccca7a21",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysLapras.Name",
    display_name="Misty's Lapras",
    searchable_by=["Misty's Lapras", "Basic", "MistysLapras"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title="Swim Together",
            game_text="Search your deck for up to 3 Misty's Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
