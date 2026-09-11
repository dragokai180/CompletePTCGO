from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='358da1fd-9ee6-51b2-b333-c064d5ff1b8d',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MetalCoreBarrier.Name',
    display_name='Metal Core Barrier',
    searchable_by=['Metal Core Barrier', 'Pokémon Tool', 'MetalCoreBarrier'],
    subtypes=['Pokémon Tool'],
    collector_number=180,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn. The Metal Pokémon this card is attached to takes 70 less damage from your opponent's attacks (after applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
