from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f898599a-60e0-536e-a55b-cd59b31e283f',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LucarioSpiritLink.Name',
    display_name='Lucario Spirit Link',
    searchable_by=['Lucario Spirit Link', 'Pokémon Tool', 'LucarioSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=211,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Lucario-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
