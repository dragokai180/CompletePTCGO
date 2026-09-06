from spirit.game.data_utils import PokemonToolCardDef, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class MaximumBeltPassive(Passive):
    """+50 damage to the opponent's Active Pokémon ex (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and calc.to_active
            and carrier_pokemon(carrier) is calc.attacker
            and is_pokemon_ex(calc.target.archetype_id)
        ):
            calc.amount += 50


card = PokemonToolCardDef(
    guid="63ed7f8f-b7da-5b09-8713-f68586144e87",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaximumBelt.Name",
    display_name="Maximum Belt",
    searchable_by=["Maximum Belt", "Item", "Pokémon Tool", "ACE SPEC", "MaximumBelt"],
    subtypes=["Item", "Pokémon Tool", "ACE SPEC"],
    collector_number=154,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    passive=MaximumBeltPassive(),
)
