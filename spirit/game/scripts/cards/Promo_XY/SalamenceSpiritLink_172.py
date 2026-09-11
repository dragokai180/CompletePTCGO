from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='94f2b74f-7dce-5534-b421-e611aa693cfb',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SalamenceSpiritLink.Name',
    display_name='Salamence Spirit Link',
    searchable_by=['Salamence Spirit Link', 'Pokémon Tool', 'SalamenceSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=172,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Salamence-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
