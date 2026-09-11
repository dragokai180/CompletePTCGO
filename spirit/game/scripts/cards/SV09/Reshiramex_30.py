from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="144def1a-9f8c-5f53-bb76-3f84eb188b6f",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiramex.Name",
    display_name="Reshiram ex",
    searchable_by=["Reshiram ex", "Basic", "ex", "Reshiramex"],
    subtypes=["Basic", "ex"],
    collector_number=30,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
        Attack(
            title="Scorching Fire",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
