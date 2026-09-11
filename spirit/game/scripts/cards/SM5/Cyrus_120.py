from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4e7ff502-56ef-5e9c-aaaf-42e068e827a4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Cyrus.Name',
    display_name='Cyrus ◇',
    searchable_by=['Cyrus ◇', 'Supporter', 'Prism Star', 'Cyrus'],
    subtypes=['Supporter', 'Prism Star'],
    collector_number=120,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Prism,
    effect=standard_trainer_effect("You can play this card only if your Active Pokémon is a Water or Metal Pokémon. Your opponent chooses 2 Benched Pokémon and shuffles the others, and all cards attached to them, into their deck. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
    condition=standard_trainer_condition("You can play this card only if your Active Pokémon is a Water or Metal Pokémon. Your opponent chooses 2 Benched Pokémon and shuffles the others, and all cards attached to them, into their deck. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
