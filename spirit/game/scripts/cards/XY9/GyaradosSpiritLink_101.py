from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='961fe2e5-7fe1-5bc4-9079-a98901a6ed54',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GyaradosSpiritLink.Name',
    display_name='Gyarados Spirit Link',
    searchable_by=['Gyarados Spirit Link', 'Pokémon Tool', 'GyaradosSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=101,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Gyarados-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
