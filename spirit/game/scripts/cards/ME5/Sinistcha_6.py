from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.passives_common import (
    count_hide_n_sneak_in_discard, full_effect_shield_passive,
)


async def matcha_spin(ctx):
    """If you have 6 or more Pokémon that have Hide 'n' Sneak in your discard
    pile, place 4 damage counters on each of your opponent's Pokémon."""
    if count_hide_n_sneak_in_discard(ctx) < 6:
        return
    await place_counters(4, "each_opponent")(ctx)


card = PokemonCardDef(
    guid="b14ebb0e-39e9-5b5f-9819-b4130448ac65",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistcha.Name",
    display_name="Sinistcha",
    searchable_by=["Sinistcha","Stage 1","Sinistcha"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=1012,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pokémon's attacks and Abilities done to this Pokémon. (Damage is not an effect.)",
            passive=full_effect_shield_passive(),
        ),
        Attack(
            title="Matcha Spin",
            game_text="If you have 6 or more Pokémon that have the Hide 'n' Sneak Ability in your discard pile, place 4 damage counters on each of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=matcha_spin,
        ),
    ],
)
