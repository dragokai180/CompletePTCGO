from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c9203381-c2fa-5d40-82fd-9873cfdd94e4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStarmie.Name",
    display_name="Misty's Starmie",
    searchable_by=["Misty's Starmie", "Stage 1", "MistysStarmie"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Abrupt Flash",
            game_text="If this Pokémon evolved from Misty's Staryu during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
