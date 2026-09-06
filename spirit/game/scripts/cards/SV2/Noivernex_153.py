"""Noivern ex (SV - Paldea Evolved 153/193).

Stage 1 Dragon Pokemon ex, evolves from Noibat. HP 260, no weakness, no
resistance, free retreat.

  Covert Flight   [CC]  70   During your opponent's next turn, prevent all
                             damage done to this Pokemon by attacks from
                             Basic Pokemon.
  Dominating Echo [PD] 140   During your opponent's next turn, they can't
                             play any Special Energy or Stadium cards from
                             their hand.

Covert Flight prints the same sentence as Flying Pikachu VMAX's Max Balloon,
so both now run the shared shield_from_basics rather than spelling the
predicate out twice.

Dominating Echo is Budew's play lock with a two-card predicate. The engine
consults the same lock for Energy attachments and Stadium plays as for
Trainer plays, so one lock_plays call covers both halves of the sentence.

This is the first card from Paldea Evolved; the set is registered in
sets.json alongside the other post-shutdown sets the project already carries.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import shield_from_basics
from spirit.game.session.effects import is_special_energy, is_stadium_card


def _special_energy_or_stadium(card) -> bool:
    return is_special_energy(card) or is_stadium_card(card)


async def dominating_echo(ctx):
    """140. No Special Energy and no Stadium from their hand next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _special_energy_or_stadium)


card = PokemonCardDef(
    guid="4015f090-2918-57da-b926-bb8ac956ec99",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivernex.Name",
    display_name="Noivern ex",
    searchable_by=["Noivern ex", "Stage 1", "ex", "Noivernex"],
    subtypes=["Stage 1", "ex"],
    collector_number=153,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Covert Flight",
            game_text=(
                "During your opponent's next turn, prevent all damage done "
                "to this Pokémon by attacks from Basic Pokémon."
            ),
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=shield_from_basics,
        ),
        Attack(
            title="Dominating Echo",
            game_text=(
                "During your opponent's next turn, they can't play any "
                "Special Energy or Stadium cards from their hand."
            ),
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=140,
            effect=dominating_echo,
        ),
    ],
)
