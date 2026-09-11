from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f7eb4870-efd0-5bc8-8935-276dd4c90248',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name',
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", 'Supporter', 'ErikasHospitality'],
    subtypes=['Supporter'],
    collector_number=140,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect("You can play this card only if you have 4 or fewer other cards in your hand. Draw a card for each of your opponent's Pokémon in play."),
    condition=standard_trainer_condition("You can play this card only if you have 4 or fewer other cards in your hand. Draw a card for each of your opponent's Pokémon in play."),
)
