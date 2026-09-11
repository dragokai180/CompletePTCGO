from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f9522309-7180-549a-89b2-c895b0f158dd',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PsychicMemory.Name',
    display_name='Psychic Memory',
    searchable_by=['Psychic Memory', 'Pokémon Tool', 'PsychicMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=98,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Psychic Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
