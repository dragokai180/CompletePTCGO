from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='fc22b6a2-1070-5011-be88-374afbfae4bc',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name',
    display_name='Escape Board',
    searchable_by=['Escape Board', 'Pokémon Tool', 'EscapeBoard'],
    subtypes=['Pokémon Tool'],
    collector_number=122,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of the Pokémon this card is attached to is Colorless less, and it can retreat even if it's Asleep or Paralyzed. You may play as many Item cards as you like during your turn (before your attack)."),
)
