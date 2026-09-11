from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='12426934-c087-57bc-afef-a4042c424aed',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DashingPouch.Name',
    display_name='Dashing Pouch',
    searchable_by=['Dashing Pouch', 'Pokémon Tool', 'DashingPouch'],
    subtypes=['Pokémon Tool'],
    collector_number=92,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If the Pokémon this card is attached to discards Energy for its Retreat Cost, put that Energy into your hand instead of the discard pile. You may play as many Item cards as you like during your turn (before your attack).'),
)
