from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1fc05985-a25a-5825-a3eb-e83c8ae36363',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name',
    display_name='Zinnia',
    searchable_by=['Zinnia', 'Supporter', 'Zinnia'],
    subtypes=['Supporter'],
    collector_number=64,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Attach up to 2 basic Energy cards from your hand to 1 of your Dragon Pokémon."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Attach up to 2 basic Energy cards from your hand to 1 of your Dragon Pokémon."),
)
