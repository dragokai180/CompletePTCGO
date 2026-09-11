from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='d7db8c35-7eef-5a9a-a11b-bbc9b126fb4b',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GiovannisCharisma.Name',
    display_name="Giovanni's Charisma",
    searchable_by=["Giovanni's Charisma", 'Supporter', 'GiovannisCharisma'],
    subtypes=['Supporter'],
    collector_number=161,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put an Energy attached to your opponent's Active Pokémon into their hand. If you do, attach an Energy card from your hand to your Active Pokémon."),
    condition=standard_trainer_condition("Put an Energy attached to your opponent's Active Pokémon into their hand. If you do, attach an Energy card from your hand to your Active Pokémon."),
)
