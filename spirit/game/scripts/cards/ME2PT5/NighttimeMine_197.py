from spirit.game.data_utils import StadiumCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class NighttimeMinePassive(Passive):
    """Attacks used by each Tera Pokémon in play cost Colorless more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if "Tera" in subtypes_for(pokemon.archetype_id):
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = StadiumCardDef(
    guid="54ec5ad4-248c-5e94-a4dc-82fc3847da14",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NighttimeMine.Name",
    display_name="Nighttime Mine",
    searchable_by=["Nighttime Mine", "Stadium", "NighttimeMine"],
    subtypes=["Stadium"],
    collector_number=197,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=NighttimeMinePassive(),
)
