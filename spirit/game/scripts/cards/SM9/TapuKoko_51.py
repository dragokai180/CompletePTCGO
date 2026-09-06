"""Tapu Koko ◇ (SM - Team Up 51/181).

Basic Lightning Pokemon, Prism Star. HP 130, weakness Fighting x2,
resistance Metal -20, retreat 1.

  Dance of the Ancients (Ability)  Once during your turn (before your
                        attack), if this Pokemon is on your Bench, you may
                        choose 2 of your Benched Pokemon and attach a [L]
                        Energy card from your discard pile to each of them.
                        If you do, discard all cards from this Pokemon and
                        put it in the Lost Zone.
  Mach Bolt      [LLC] 120

The self-removal needs no special handling. "Discard all cards from this
Pokemon and put it in the Lost Zone" is one discard_cards call over the
whole stack: _move_to_public_pile asks discard_area_name per card, so the
attachments land in the discard and this card, being a Prism Star, lands in
the Lost Zone. The card's two sentences fall out of one rule.

The condition demands everything the effect needs -- this Pokemon benched,
two Benched Pokemon to choose, and two [L] Energy in the discard -- so the
Ability is never offered as a play that cannot be completed.

Tapu Koko itself is a legal choice for one of the two: it is a Benched
Pokemon, the text does not exclude it, and the Energy simply leaves with it.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack, is_energy_of_type


def _lightning_in_discard(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else [])
            if is_energy_of_type(c, PokemonTypes.LIGHTNING)]


def _dance_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    benched = list(bench.children) if bench else []
    if pokemon is not None and pokemon not in benched:
        return False
    return len(benched) >= 2 and len(_lightning_in_discard(board, player_id)) >= 2


async def dance_of_the_ancients(ctx):
    """Two [L] out of the discard onto two Benched Pokemon; this card leaves."""
    koko = ctx.source
    targets = await ctx.choose_cards(
        ctx.my_bench(), 2, minimum=2,
        prompt="Choose 2 of your Benched Pokémon to attach a {L} Energy to.",
    )
    if len(targets) < 2:
        return
    energies = _lightning_in_discard(ctx.board, ctx.player_id)
    for target, energy in zip(targets, energies):
        await ctx.attach_energy(energy, target)
    # One call: the attachments go to the discard, this card to the Lost Zone.
    await ctx.discard_cards(full_stack(koko))


card = PokemonCardDef(
    guid="9d2bbe40-28d9-565f-a183-c21c970371b2",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoPrismStar.Name",
    display_name="Tapu Koko {*}",
    searchable_by=["Tapu Koko", "Basic", "Prism Star"],
    subtypes=["Basic", "Prism Star"],
    collector_number=51,
    set_code="SM9",
    rarity=Rarities.Prism,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=785,
    abilities=[
        Ability(
            title="Dance of the Ancients",
            game_text=(
                "Once during your turn (before your attack), if this Pokémon "
                "is on your Bench, you may choose 2 of your Benched Pokémon "
                "and attach a {L} Energy card from your discard pile to each "
                "of them. If you do, discard all cards from this Pokémon and "
                "put it in the Lost Zone."
            ),
            activation=Activations.ONCE_PER_TURN,
            condition=_dance_condition,
            effect=dance_of_the_ancients,
        ),
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
