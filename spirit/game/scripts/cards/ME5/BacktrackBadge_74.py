from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class BacktrackBadgePassive(Passive):
    """Once during your turn, after you flip coins for an attack of the
    Colorless Pokémon this card is attached to, you may ignore the results
    and flip again."""

    def offers_attack_coin_reroll(self, player_id, carrier, attacker=None):
        holder = carrier_pokemon(carrier)
        if holder is None or holder.owning_player_id != player_id:
            return False
        types = holder.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.COLORLESS.value not in types:
            return False
        if attacker is not None and attacker is not holder:
            return False
        return True


card = PokemonToolCardDef(
    guid="158f69a0-9205-528b-a4bc-464c562c0af9",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BacktrackBadge.Name",
    display_name="Backtrack Badge",
    searchable_by=["Backtrack Badge","Pokémon Tool","Tool","BacktrackBadge"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=74,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    passive=BacktrackBadgePassive(),
)
