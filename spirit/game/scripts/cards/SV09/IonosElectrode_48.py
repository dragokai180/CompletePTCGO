from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="92cdf8e2-2595-5e90-a214-832584b599a6",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosElectrode.Name",
    display_name="Iono's Electrode",
    searchable_by=["Iono's Electrode", "Stage 1", "IonosElectrode"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosVoltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Thump-Thump Boom",
            game_text="This Pokémon does 100 damage to itself. Flip a coin. If heads, your opponent's Active Pokémon is Knocked Out.",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=standard_attack,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
