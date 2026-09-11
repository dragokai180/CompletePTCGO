from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='681302e4-2283-5bc9-bc88-945720719652',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AlakazamSpiritLink.Name',
    display_name='Alakazam Spirit Link',
    searchable_by=['Alakazam Spirit Link', 'Pokémon Tool', 'AlakazamSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=90,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Alakazam-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
