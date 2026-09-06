from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive


class LivelyStadiumPassive(Passive):
    """Each Basic Pokémon in play (both sides) gets +30 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        return 30 if is_basic_pokemon(pokemon) else 0


card = StadiumCardDef(
    guid="f291686b-ab9d-55e2-b75b-ab1db734f26e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LivelyStadium.Name",
    display_name="Lively Stadium",
    searchable_by=["Lively Stadium", "Stadium", "LivelyStadium"],
    subtypes=["Stadium"],
    collector_number=180,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=LivelyStadiumPassive(),
)
