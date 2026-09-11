from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="ad1ca31c-beb6-54df-a1de-88bc52c28372",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AwakeningDrum.Name",
    display_name="Awakening Drum",
    searchable_by=["Awakening Drum", "Item", "Ancient", "ACE SPEC", "AwakeningDrum"],
    subtypes=["Item", "Ancient", "ACE SPEC"],
    collector_number=141,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("Draw a card for each of your Ancient Pokémon in play. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
