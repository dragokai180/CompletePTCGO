"""Ditto ◇ (SM - Lost Thunder 154/214).

Basic Colorless Pokemon, Prism Star. HP 40, weakness Fighting x2, retreat 1,
no attacks.

  Almighty Evolution (Ability)  Once during your turn (before your attack),
                        you may put any Stage 1 card from your hand onto this
                        Pokemon to evolve it. You can't use this Ability
                        during your first turn or the turn this Pokemon was
                        put into play.

Written as a passive rather than an activated Ability, because what it
actually changes is which evolutions the engine will offer: Eevee ex's
Rainbow DNA already answers may_be_evolved_into for exactly this, and
legal_actions consults it alongside the ordinary name match. The player then
evolves by dragging the Stage 1 onto this card, which is the real card's UX.

Every restriction the text spells out is the ordinary evolution rule, so
none of it needs code:

  - "during your first turn"                  -> the turn-number gate
  - "the turn this Pokemon was put into play" -> may_evolve_target
  - "once during your turn"                   -> after evolving, this card is
    a tucked pre-evolution and contributes no passives, so it cannot happen
    twice

Being a Prism Star Pokemon, it is the first card to exercise the Lost Zone
rule on a knockout: resolve_knockouts now routes any stack member that would
reach a discard pile to the Lost Zone if it is a Prism Star.
"""

from spirit.game.data_utils import PokemonCardDef, Ability
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _AlmightyEvolutionPassive(Passive):
    """Any Stage 1 card may be put onto this Pokemon to evolve it."""

    def may_be_evolved_into(self, pokemon, carrier, evolution_card):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        return evolution_card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value


card = PokemonCardDef(
    guid="600ddbd8-4185-502c-a662-cfdae26dc68f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoPrismStar.Name",
    display_name="Ditto {*}",
    searchable_by=["Ditto", "Basic", "Prism Star"],
    subtypes=["Basic", "Prism Star"],
    collector_number=154,
    set_code="SM8",
    rarity=Rarities.Prism,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Almighty Evolution",
            game_text=(
                "Once during your turn (before your attack), you may put any "
                "Stage 1 card from your hand onto this Pokémon to evolve it. "
                "You can't use this Ability during your first turn or the "
                "turn this Pokémon was put into play."
            ),
            passive=_AlmightyEvolutionPassive(),
        ),
    ],
)
