"""Tapu Lele-GX (SM - Guardians Rising 60/145).

Basic Psychic Pokemon-GX. HP 170, no weakness, no resistance, retreat 1.

  Wonder Tag (Ability)  When you play this Pokemon from your hand onto
                        your Bench during your turn, you may search your
                        deck for a Supporter card, reveal it, and put it
                        into your hand. Then, shuffle your deck.
  Energy Drive     [CC] 20x  This attack does 20 damage times the amount
                        of Energy attached to both Active Pokemon. This
                        damage isn't affected by Weakness or Resistance.
  Tapu Cure-GX     [P]   Heal all damage from 2 of your Benched Pokemon.
                        (You can't use more than 1 GX attack in a game.)

Wonder Tag is Lumineon V's Luminous Sign verbatim -- same trigger, same
body -- so it reuses luminous_sign. Note there is NO shared_once_per_turn
here: unlike Crobat V's Dark Asset or Meowth ex's Last-Ditch Catch, this
card's text carries no "you can't use more than 1 ... each turn" clause,
so two Tapu Lele-GX benched in one turn each get their search.

Energy Drive counts PROVIDED Energy (count_energy's default), so a Double
Colorless on either Active counts as 2 -- which is the ruling. There is no
count_energy scope for "both Actives" (its "both" means every Pokemon in
play), hence the two-scope sum.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.pokemon import luminous_sign

_energy_on_my_active = count_energy("my_active")
_energy_on_defender = count_energy("defender")


def _energy_on_both_actives(ctx) -> int:
    return _energy_on_my_active(ctx) + _energy_on_defender(ctx)


async def energy_drive(ctx):
    """20 damage per Energy on both Actives; no Weakness or Resistance."""
    amount = 20 * _energy_on_both_actives(ctx)
    if amount > 0:
        await ctx.deal_damage(
            amount, ignore_weakness=True, ignore_resistance=True,
        )


async def tapu_cure_gx(ctx):
    """Heal all damage from 2 of your Benched Pokemon."""
    damaged = [
        p for p in ctx.my_bench()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not damaged:
        return
    picks = await ctx.choose_cards(
        damaged, 2, minimum=0,
        prompt="Choose up to 2 of your Benched Pokémon to heal.",
    )
    for pokemon in picks:
        missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, pokemon)


card = PokemonCardDef(
    guid="b95990f8-b700-53f7-9345-d39287089c84",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLeleGX.Name",
    display_name="Tapu Lele-GX",
    searchable_by=["Tapu Lele-GX", "Basic", "GX", "TapuLeleGX"],
    subtypes=["Basic", "GX"],
    collector_number=60,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=786,
    abilities=[
        Ability(
            title="Wonder Tag",
            game_text=(
                "When you play this Pokémon from your hand onto your "
                "Bench during your turn, you may search your deck for a "
                "Supporter card, reveal it, and put it into your hand. "
                "Then, shuffle your deck."
            ),
            trigger=Triggers.ON_PLAY,
            effect=luminous_sign,
        ),
        Attack(
            title="Energy Drive",
            game_text=(
                "This attack does 20 damage times the amount of Energy "
                "attached to both Active Pokémon. This damage isn't "
                "affected by Weakness or Resistance."
            ),
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=energy_drive,
        ),
        Attack(
            title="Tapu Cure-GX",
            game_text=(
                "Heal all damage from 2 of your Benched Pokémon. (You "
                "can't use more than 1 GX attack in a game.)"
            ),
            cost={PokemonTypes.PSYCHIC: 1},
            gx=True,
            effect=tapu_cure_gx,
        ),
    ],
)
