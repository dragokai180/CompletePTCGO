from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='06cf15ae-a698-5e9a-aca6-5cbeda20e770',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name',
    display_name='Karate Belt',
    searchable_by=['Karate Belt', 'Pokémon Tool', 'KarateBelt'],
    subtypes=['Pokémon Tool'],
    collector_number=201,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If you have more Prize cards remaining than your opponent, the attacks of the Pokémon this card is attached to cost Fighting less. You may play as many Item cards as you like during your turn (before your attack).'),
)
