from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='42e94428-abd4-539d-ad6b-d0c8f89d9855',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MewtwoSpiritLink.Name',
    display_name='Mewtwo Spirit Link',
    searchable_by=['Mewtwo Spirit Link', 'Pokémon Tool', 'MewtwoSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=144,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Mewtwo-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
