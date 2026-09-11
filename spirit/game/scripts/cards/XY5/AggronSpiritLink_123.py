from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f77d9ee0-9cce-5327-b761-1daf01b36b05',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AggronSpiritLink.Name',
    display_name='Aggron Spirit Link',
    searchable_by=['Aggron Spirit Link', 'Pokémon Tool', 'AggronSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=123,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Aggron-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
