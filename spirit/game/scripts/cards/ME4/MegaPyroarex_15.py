from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="51a83341-7607-5e02-a526-ae40f0cc26f3",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaPyroarex.Name",
    display_name="Mega Pyroar ex",
    searchable_by=["Mega Pyroar ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaPyroarex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=15,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Ferocious Bellow",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title="Fiery Big Bang",
            game_text="This attack does 10 less damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=290,
            damage_operator="-",
            effect=standard_attack,
        ),
    ],
)
