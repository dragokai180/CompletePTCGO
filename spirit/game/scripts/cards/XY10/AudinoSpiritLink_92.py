from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='26df2f58-323a-5027-973f-e8969c4c3fdd',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AudinoSpiritLink.Name',
    display_name='Audino Spirit Link',
    searchable_by=['Audino Spirit Link', 'Pokémon Tool', 'AudinoSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=92,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Audino-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
