"""Black Market ◇ (SM - Team Up 134/181).

Stadium, Prism Star.

  "When a Darkness Pokemon (yours or your opponent's) that has any Darkness
   Energy attached to it is Knocked Out by damage from an opponent's attack,
   that player takes 1 fewer Prize card."
  "Whenever any player plays an Item or Supporter card from their hand,
   prevent all effects of that card done to this Stadium card."

The second sentence is word for word Thunder Mountain's, so both Prism Star
Stadiums now inherit ShieldedStadiumPassive rather than repeating it.

The prize clause is Lillie's Pearl's hook with a different filter, and the
"by damage from an opponent's attack" gate reads the same way. "Any Darkness
Energy attached" goes through energy_provides_type rather than the card's
printed type, so a Special Energy that provides [D] -- Legacy Energy, which
provides every type -- counts, which is the ruling.

Worth knowing when both are on the board: the reduction floors at zero, and
Legacy Energy spends its own once-per-game whenever it fires, so a Darkness
Pokemon carrying Legacy Energy under this Stadium wastes the Energy's
one use. A test pins that down.
"""

from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import BlackMarketPassive

card = StadiumCardDef(
    passive=BlackMarketPassive(),
    guid="8713634e-a490-56c7-b72f-a119019d7101",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackMarketPrismStar.Name",
    display_name="Black Market {*}",
    searchable_by=["Black Market", "Stadium", "Prism Star", "BlackMarket"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=134,
    set_code="SM9",
    rarity=Rarities.Prism,
)
