from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='3afe7f14-cec5-5487-b190-e53ffd5fbfa2',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HealingScarf.Name',
    display_name='Healing Scarf',
    searchable_by=['Healing Scarf', 'Pokémon Tool', 'HealingScarf'],
    subtypes=['Pokémon Tool'],
    collector_number=84,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Whenever you attach an Energy card from your hand to the Pokémon this card is attached to, heal 20 damage from it. You may play as many Item cards as you like during your turn (before your attack).'),
)
