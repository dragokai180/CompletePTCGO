from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='ce1df9ad-1903-533a-b49d-895a74318263',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TyranitarSpiritLink.Name',
    display_name='Tyranitar Spirit Link',
    searchable_by=['Tyranitar Spirit Link', 'Pokémon Tool', 'TyranitarSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=81,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Tyranitar-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
