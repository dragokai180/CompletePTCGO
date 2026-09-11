from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ec928c3d-641a-5888-b50a-31a3ff875c1f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWake.Name",
    display_name="Walking Wake",
    searchable_by=["Walking Wake", "Basic", "Ancient", "WalkingWake"],
    subtypes=["Basic", "Ancient"],
    collector_number=63,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=1009,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Undulating Slice",
            game_text="Put up to 9 damage counters on this Pokémon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
