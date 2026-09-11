from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0ef0f6a3-ae8c-53bb-82f5-92541b5f3e7e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTailex.Name",
    display_name="Scream Tail ex",
    searchable_by=["Scream Tail ex", "Basic", "ex", "Ancient", "ScreamTailex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=94,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=985,
    abilities=[
        Attack(
            title="Scream",
            game_text="You can use this attack only if you go second, and only during your first turn. Your opponent can't play any Supporter cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
