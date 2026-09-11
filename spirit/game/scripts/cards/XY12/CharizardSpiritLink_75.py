from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='6eb65d69-d4c2-542e-9b4f-3dd9aa912271',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CharizardSpiritLink.Name',
    display_name='Charizard Spirit Link',
    searchable_by=['Charizard Spirit Link', 'Pokémon Tool', 'CharizardSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=75,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Charizard-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
