"""Oricorio-GX (SM - Cosmic Eclipse 95/236).

Basic Psychic Pokemon-GX. HP 170, weakness Darkness x2, resistance
Fighting -20, retreat 1.

  Dance of Tribute (Ability)  Once during your turn (before your attack),
                        if any of your Pokemon were Knocked Out during your
                        opponent's last turn, you may draw 3 cards. You
                        can't use more than 1 Dance of Tribute Ability each
                        turn.
  Razor Wing   [PCC]  80
  Strafe-GX    [PCC] 100  Switch this Pokemon with 1 of your Benched
                        Pokemon. (You can't use more than 1 GX attack in a
                        game.)

Dance of Tribute is Fezandipiti ex's Flip the Script word for word, so the
"were Knocked Out during your opponent's last turn" test now lives in
card_effects/pokemon.py as ally_ko_last_turn and both cards read it from
there. shared_once_per_turn carries the "not more than 1 each turn" clause,
which is what stops two copies on the bench from drawing 6.

Strafe-GX is switch_self_attack with no damage argument, so it deals the
Attack's own printed 100 before the switch, in text order.

The Fighting -20 resistance is printed as-is. Marshadow (SM8 81) already
carries Fighting -20 in this pool and saves to a deck without trouble, and
passives.py reads a card's own RESISTANCE_AMOUNT rather than assuming 30.
"""

from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.card_effects.support_common import switch_self_attack


async def dance_of_tribute(ctx):
    await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="b61f54af-5c81-5151-b735-aa976dbc4523",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OricorioGX.Name",
    display_name="Oricorio-GX",
    searchable_by=["Oricorio-GX", "Basic", "GX", "OricorioGX"],
    subtypes=["Basic", "GX"],
    collector_number=95,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Ability(
            title="Dance of Tribute",
            game_text=(
                "Once during your turn (before your attack), if any of your "
                "Pokémon were Knocked Out during your opponent's last turn, "
                "you may draw 3 cards.\n\nYou can't use more than 1 Dance of "
                "Tribute Ability each turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Dance of Tribute",
            condition=ally_ko_last_turn,
            effect=dance_of_tribute,
        ),
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Strafe-GX",
            game_text=(
                "Switch this Pokémon with 1 of your Benched Pokémon. "
                "(You can't use more than 1 GX attack in a game.)"
            ),
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            gx=True,
            effect=switch_self_attack(),
        ),
    ],
)
