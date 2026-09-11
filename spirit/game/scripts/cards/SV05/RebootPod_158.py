from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="e74b1a10-66f3-56ec-9833-3992e2bb1c15",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RebootPod.Name",
    display_name="Reboot Pod",
    searchable_by=["Reboot Pod", "Item", "Future", "ACE SPEC", "RebootPod"],
    subtypes=["Item", "Future", "ACE SPEC"],
    collector_number=158,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("Attach a Basic Energy card from your discard pile to each of your Future Pokémon. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
