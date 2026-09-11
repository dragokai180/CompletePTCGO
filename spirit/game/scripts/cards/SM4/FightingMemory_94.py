from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='d246a228-e265-54ee-a7e9-b3bd6884945e',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FightingMemory.Name',
    display_name='Fighting Memory',
    searchable_by=['Fighting Memory', 'Pokémon Tool', 'FightingMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=94,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Fighting Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
