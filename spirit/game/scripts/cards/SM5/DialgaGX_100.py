"""Dialga-GX (SM - Ultra Prism 100/156) -- the DRAGON-type print.

Dialga-GX was printed twice with identical attacks but different types:
  - Forbidden Light 82/131: Metal type, weak to Fire, resist Psychic -20.
  - Ultra Prism  100/156:  Dragon type, weak to Fairy, no resistance.

Regidrago VSTAR's "Apex Dragon" can only copy attacks from a DRAGON-type
Pokemon sitting in the discard pile, so this deck needs the Ultra Prism
(Dragon) print specifically -- the Forbidden Light (Metal) print is a
different, unrelated card as far as that attack is concerned.

Dragon Basic Pokemon-GX. HP 180, weakness Fairy x2, no resistance,
retreat cost 3.

  Overclock          [M]      Draw cards until you have 6 cards in hand.
  Shred               [MM]    80 damage. Not affected by any effects on the
                               opponent's Active Pokemon.
  Timeless-GX         [MMMCC] 150 damage. Take another turn after this one.
                               (You can't use more than 1 GX attack in a game.)

Place this file at:
  spirit/game/scripts/cards/SM5/DialgaGX_100.py
and the matching 1024x1024 art at:
  spirit/assets/cards/SM5/DialgaGX_100.png

NOTE: sets.json registers Ultra Prism under the canonical name "SM5"
("UPR" only exists there as an externalId alias, not a usable set_code/key
for AutoBundle purposes) -- diagnose_sets.py confirmed this. Using "UPR"
as set_code/key let the card register and transmit its data fine, but
AutoBundle's asset-bundle generation never recognized "UPR" as a real
set, so the card art was never bundled. "SM5" is the value that matches.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def overclock(ctx):
    """Draw cards until you have 6 cards in your hand."""
    await ctx.draw_until(6)


async def shred(ctx):
    """80 damage; ignores any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)


async def timeless_gx(ctx):
    """150 damage, then take another turn after this one.

    The "you can't use more than 1 GX attack in a game" restriction is
    enforced by the engine itself (Attack.gx=True below) -- this effect
    only needs to resolve the damage and the extra turn.
    """
    await ctx.deal_damage()
    ctx.take_extra_turn()


card = PokemonCardDef(
    guid="550ad86f-0d5c-4c56-bd9a-bdb24d41490b",
    key="SM5",
    name="Dialga-GX",
    display_name="Dialga-GX",
    collector_number=100,
    set_code="SM5",
    # Rare Holo GX per the printed card; it was filed as RareUltra, which is
    # the client's "Full Art" rarity. (This does not restore the deck
    # builder's "Pokemon-GX" filter -- pie-src.dll has no GX predicate at
    # all, so that row matches nothing whatever the server sends.)
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=483,
    abilities=[
        Attack(
            title="Overclock",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.METAL: 1},
            effect=overclock,
        ),
        Attack(
            title="Shred",
            game_text=(
                "This attack's damage isn't affected by any effects on "
                "your opponent's Active Pokemon."
            ),
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=shred,
        ),
        Attack(
            title="Timeless-GX",
            game_text=(
                "Take another turn after this one. (Skip the between "
                "turns step.) (You can't use more than 1 GX attack in "
                "a game.)"
            ),
            cost={
                PokemonTypes.METAL: 3,
                PokemonTypes.COLORLESS: 2,
            },
            damage=150,
            gx=True,
            effect=timeless_gx,
        ),
    ],
)
