from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import any_type_attack_discount


card = PokemonToolCardDef(
    guid="f1701199-f96d-5c00-8ca4-85a180b60a08",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SparklingCrystal.Name",
    display_name="Sparkling Crystal",
    searchable_by=[
        "Sparkling Crystal", "Item", "Pokémon Tool", "ACE SPEC", "SparklingCrystal",
    ],
    subtypes=["Item", "Pokémon Tool", "ACE SPEC"],
    collector_number=142,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    passive=any_type_attack_discount(
        1, holder_pred=lambda p: "Tera" in subtypes_for(p.archetype_id),
    ),
)
