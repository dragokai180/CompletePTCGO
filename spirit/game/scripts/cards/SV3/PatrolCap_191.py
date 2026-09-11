from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='b763bd6b-c55e-53fa-826d-9e1fd920470c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PatrolCap.Name',
    display_name='Patrol Cap',
    searchable_by=['Patrol Cap', 'Pokémon Tool', 'PatrolCap'],
    subtypes=['Pokémon Tool'],
    collector_number=191,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("As long as the Pokémon this card is attached to is in the Active Spot, cards in your deck can't be discarded by effects of your opponent's attacks, Abilities, Item cards, Pokémon Tool cards, or Supporter cards."),
)
