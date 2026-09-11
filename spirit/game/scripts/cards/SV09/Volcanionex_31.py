from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bc5d25ea-f20d-51b2-9980-958c953acb5b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanionex.Name",
    display_name="Volcanion ex",
    searchable_by=["Volcanion ex", "Basic", "ex", "Volcanionex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Ability(
            title="Scalding Steam",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Burned.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Scorching Cyclone",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
