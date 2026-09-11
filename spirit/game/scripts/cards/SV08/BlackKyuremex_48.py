from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1a523e71-4d65-535c-9812-20afaa18f6d7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremex.Name",
    display_name="Black Kyurem ex",
    searchable_by=["Black Kyurem ex", "Basic", "ex", "BlackKyuremex"],
    subtypes=["Basic", "ex"],
    collector_number=48,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title="Ice Age",
            game_text="If your opponent's Active Pokémon is a Dragon Pokémon, it is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title="Black Frost",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=standard_attack,
        ),
    ],
)
