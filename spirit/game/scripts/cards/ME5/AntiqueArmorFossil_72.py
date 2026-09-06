from spirit.game.data_utils import FossilItemCardDef, Ability
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot, takes_less_passive
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.session.passives import Passive, carrier_pokemon


class ProtectiveArmorPassive(Passive):
    """While this Pokémon is Active, all of your Pokémon take 10 less damage
    from opposing attacks."""

    def __init__(self):
        self._inner = takes_less_passive(10, protects="team")

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if not is_in_active_spot(holder):
            return
        self._inner.modify_damage_taken(calc, carrier)


card = FossilItemCardDef(
    guid="b9cea90c-cfda-587c-91a2-ffc487fbfc1f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueArmorFossil.Name",
    display_name="Antique Armor Fossil",
    searchable_by=["Antique Armor Fossil","Item","AntiqueArmorFossil"],
    subtypes=["Item"],
    collector_number=72,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Protective Armor",
            game_text="As long as this Pokémon is in the Active Spot, all of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=ProtectiveArmorPassive(),
        ),
    ],
)
