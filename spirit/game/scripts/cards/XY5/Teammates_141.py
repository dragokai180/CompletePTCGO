from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='846718aa-ccef-5fe9-9a33-647af4f4e0dc',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name',
    display_name='Teammates',
    searchable_by=['Teammates', 'Supporter', 'Teammates'],
    subtypes=['Supporter'],
    collector_number=141,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward."),
)
