from spirit.game.data_utils import PokemonToolCardDef, has_rule_box, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class BraveBanglePassive(Passive):
    """If the holder has no Rule Box, its attacks do +30 to the opponent's
    Active Pokémon ex (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not calc.attacker:
            return
        if has_rule_box(holder.archetype_id):
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.target is not None and is_pokemon_ex(calc.target.archetype_id):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="5c528680-2b43-5eb1-9abf-e1a3fa2073ef",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveBangle.Name",
    display_name="Brave Bangle",
    searchable_by=["Brave Bangle","Pokémon Tool","Tool","BraveBangle"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=80,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=BraveBanglePassive(),
)
