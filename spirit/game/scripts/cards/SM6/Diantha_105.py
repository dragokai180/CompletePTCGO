from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='3cc15279-2c3e-50aa-960c-1fc236e33ca7',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name',
    display_name='Diantha',
    searchable_by=['Diantha', 'Supporter', 'Diantha'],
    subtypes=['Supporter'],
    collector_number=105,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect("You can play this card only if 1 of your Fairy Pokémon was Knocked Out during your opponent's last turn. Put 2 cards from your discard pile into your hand."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Fairy Pokémon was Knocked Out during your opponent's last turn. Put 2 cards from your discard pile into your hand."),
)
