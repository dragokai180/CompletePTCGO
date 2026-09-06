from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


class GravityGemstonePassive(Passive):
    """Holder's Retreat Cost is [C] more, and the opponent's Active Pokémon's
    Retreat Cost is [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if pokemon is holder:
            return cost + 1
        if (
            holder is not None
            and is_in_active_spot(pokemon)
            and pokemon.owning_player_id != holder.owning_player_id
        ):
            return cost + 1
        return cost


card = PokemonToolCardDef(
    guid="13f5798c-8e71-51a3-afdd-a64951e9fdbb",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GravityGemstone.Name",
    display_name="Gravity Gemstone",
    searchable_by=["Gravity Gemstone","Pokémon Tool","Tool","GravityGemstone"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=137,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=GravityGemstonePassive(),
)
