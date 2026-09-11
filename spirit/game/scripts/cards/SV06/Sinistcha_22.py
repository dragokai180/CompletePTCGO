from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b5231a1f-91f8-5f72-948d-f820bda029f6",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistcha.Name",
    display_name="Sinistcha",
    searchable_by=["Sinistcha", "Stage 1", "Sinistcha"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    family_id=1012,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Spill the Tea",
            game_text="Discard up to 3 Grass Energy cards from your Pokémon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
