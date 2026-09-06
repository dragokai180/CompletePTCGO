from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class GravityMountainPassive(Passive):
    """Each Stage 2 Pokémon in play (both sides) gets -30 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value:
            return -30
        return 0


card = StadiumCardDef(
    guid="92e8c82b-66cd-592d-b931-1174c4e32ff8",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityMountain.Name",
    display_name="Gravity Mountain",
    searchable_by=["Gravity Mountain", "Stadium", "GravityMountain"],
    subtypes=["Stadium"],
    collector_number=177,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=GravityMountainPassive(),
)
