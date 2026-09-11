from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='00094e70-0dc4-5916-ac71-230c6bf4b10f',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ChoiceHelmet.Name',
    display_name='Choice Helmet',
    searchable_by=['Choice Helmet', 'Pokémon Tool', 'ChoiceHelmet'],
    subtypes=['Pokémon Tool'],
    collector_number=169,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Pokémon this card is attached to takes 30 less damage from the attacks of your opponent's Pokémon-GX and Pokémon-EX (after applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
