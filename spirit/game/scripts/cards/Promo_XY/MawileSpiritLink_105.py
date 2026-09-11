from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='4f4c8a47-ce25-5e47-80b2-a0747557fe79',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MawileSpiritLink.Name',
    display_name='Mawile Spirit Link',
    searchable_by=['Mawile Spirit Link', 'Pokémon Tool', 'MawileSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=105,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Mawile-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
