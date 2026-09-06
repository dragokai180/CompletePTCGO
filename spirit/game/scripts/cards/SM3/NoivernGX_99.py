"""Noivern-GX (SM - Burning Shadows 99/147).

Stage 1 Dragon Pokemon-GX, evolves from Noibat. HP 200, weakness Fairy x2,
no resistance, free retreat.

  Distort      [DC]  50   Your opponent can't play any Item cards from
                          their hand during their next turn.
  Sonic Volume [PDC] 120  Your opponent can't play any Special Energy cards
                          from their hand during their next turn.
  Boomburst-GX [PDC]      50 damage to each of your opponent's Pokemon.
                          (Don't apply Weakness and Resistance for Benched
                          Pokemon.) (You can't use more than 1 GX attack in
                          a game.)

Both locks are Budew's Itchy Pollen with a different predicate:
ctx.lock_plays(opponent, pred) runs through the opponent's next turn, and
legal_actions consults the same play lock for Energy attachments as for
Trainer plays, so is_special_energy gates Sonic Volume's half without
needing a separate mechanism.

Boomburst-GX is damage_all_opponents, whose spread already skips weakness
and resistance on Benched targets -- the parenthetical is the engine's
default, not something this card has to ask for.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.session.effects import is_item_card, is_special_energy


async def distort(ctx):
    """50. No Item cards from the opponent's hand next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


async def sonic_volume(ctx):
    """120. No Special Energy from the opponent's hand next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_special_energy)


card = PokemonCardDef(
    guid="30f1445c-ea26-556d-8703-791b8eabfbd1",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernGX.Name",
    display_name="Noivern-GX",
    searchable_by=["Noivern-GX", "Stage 1", "GX", "NoivernGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=99,
    set_code="SM3",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Distort",
            game_text=(
                "Your opponent can't play any Item cards from their hand "
                "during their next turn."
            ),
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=distort,
        ),
        Attack(
            title="Sonic Volume",
            game_text=(
                "Your opponent can't play any Special Energy cards from "
                "their hand during their next turn."
            ),
            cost={
                PokemonTypes.PSYCHIC: 1,
                PokemonTypes.DARKNESS: 1,
                PokemonTypes.COLORLESS: 1,
            },
            damage=120,
            effect=sonic_volume,
        ),
        Attack(
            title="Boomburst-GX",
            game_text=(
                "This attack does 50 damage to each of your opponent's "
                "Pokémon. (Don't apply Weakness and Resistance for Benched "
                "Pokémon.) (You can't use more than 1 GX attack in a game.)"
            ),
            cost={
                PokemonTypes.PSYCHIC: 1,
                PokemonTypes.DARKNESS: 1,
                PokemonTypes.COLORLESS: 1,
            },
            gx=True,
            effect=damage_all_opponents(50),
        ),
    ],
)
