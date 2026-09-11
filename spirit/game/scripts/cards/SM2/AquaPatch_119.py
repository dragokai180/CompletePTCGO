from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='073d26a6-da8c-5445-ab3c-897f46bc25a2',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name',
    display_name='Aqua Patch',
    searchable_by=['Aqua Patch', 'Item', 'AquaPatch'],
    subtypes=['Item'],
    collector_number=119,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach a Water Energy card from your discard pile to 1 of your Benched Water Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Attach a Water Energy card from your discard pile to 1 of your Benched Water Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
