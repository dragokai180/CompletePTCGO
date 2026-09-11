from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='7e429de7-9066-542d-b839-6c7e4177b718',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TrickCoin.Name',
    display_name='Trick Coin',
    searchable_by=['Trick Coin', 'Pokémon Tool', 'TrickCoin'],
    subtypes=['Pokémon Tool'],
    collector_number=108,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Once during your turn, after you flip any coins for an attack of the Pokémon this card is attached to, you may ignore all effects of those coin flips and begin flipping those coins again. (You may only use effects that let you flip coins again, including effects from other cards, once during your turn.) You may play as many Item cards as you like during your turn (before your attack).'),
)
