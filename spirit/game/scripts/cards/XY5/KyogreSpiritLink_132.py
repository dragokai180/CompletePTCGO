from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='35f2feb9-347d-5271-ae27-8a8b3586c8c5',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.KyogreSpiritLink.Name',
    display_name='Kyogre Spirit Link',
    searchable_by=['Kyogre Spirit Link', 'Pokémon Tool', 'KyogreSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=132,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes Primal Kyogre-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
