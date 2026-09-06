from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive


class ForestOfVitalityPassive(Passive):
    """Grass Pokémon can evolve into Grass Pokémon the turn they are played,
    except during either player's first turn."""

    def may_evolve_same_turn(self, pokemon, carrier, evolution_card):
        p_types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        e_types = evolution_card.get_attribute(AttrID.POKEMON_TYPES) or []
        return (PokemonTypes.GRASS.value in p_types
                and PokemonTypes.GRASS.value in e_types)


card = StadiumCardDef(
    guid="161ae40c-ab9e-513e-9f7a-2573a8d3dc10",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofVitality.Name",
    display_name="Forest of Vitality",
    searchable_by=["Forest of Vitality","Stadium","ForestofVitality"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=ForestOfVitalityPassive(),
)
