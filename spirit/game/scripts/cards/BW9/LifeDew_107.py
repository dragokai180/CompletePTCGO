"""Life Dew (BW - Plasma Freeze 107/116).

Pokemon Tool, ACE SPEC.

  "If the Pokemon this card is attached to is Knocked Out, your opponent
   takes 1 fewer Prize card."

Lillie's Pearl is the Tool-shaped precedent for modify_prizes_for_knockout,
and Legacy Energy carries the same sentence from a Special Energy. This one
is the plainest of the three, because its text qualifies nothing:

  - Lillie's Pearl adds "by damage from an attack from your opponent's
    Pokemon", so it checks ctx.is_attack_effect() and the attacker's side.
  - Legacy Energy's implementation also holds a once-per-game flag.
  - Life Dew says only "is Knocked Out", so neither gate belongs here. A
    Pokemon that faints to poison, or to its own attack's recoil, still
    costs the opponent a Prize.

The ACE SPEC deck limit is already enforced in game/rules.py.
"""

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _LifeDewPassive(Passive):
    """The holder's knockout is worth one Prize less, however it happened."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return count
        return max(0, count - 1)


card = PokemonToolCardDef(
    guid="691f6d4b-5916-5149-a203-625437431d99",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeDew.Name",
    display_name="Life Dew",
    searchable_by=["Life Dew", "Pokémon Tool", "ACE SPEC", "LifeDew"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=107,
    set_code="BW9",
    rarity=Rarities.Ace,
    passive=_LifeDewPassive(),
)
