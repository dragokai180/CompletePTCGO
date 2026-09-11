from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4513cdbb-3905-5083-b86c-62d5da2e411e",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future", "IronMoth"],
    subtypes=["Basic", "Future"],
    collector_number=9,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=994,
    abilities=[
        Attack(
            title="Suction",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title="Anachronism Repulsor",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Ancient Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
