from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='18d0ecbd-9773-54b3-a02e-b41d581505ad',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ScizorSpiritLink.Name',
    display_name='Scizor Spirit Link',
    searchable_by=['Scizor Spirit Link', 'Pokémon Tool', 'ScizorSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=111,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Scizor-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
