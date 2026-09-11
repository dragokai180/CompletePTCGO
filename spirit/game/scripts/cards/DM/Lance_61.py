from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e3ebff2a-f53c-550d-afcf-caf8d079d6ab',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lance.Name',
    display_name='Lance ◇',
    searchable_by=['Lance ◇', 'Supporter', 'Prism Star', 'Lance'],
    subtypes=['Supporter', 'Prism Star'],
    collector_number=61,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Prism,
    effect=standard_trainer_effect("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for up to 2 Dragon Pokémon and put them onto your Bench. Then, shuffle your deck. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for up to 2 Dragon Pokémon and put them onto your Bench. Then, shuffle your deck. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
