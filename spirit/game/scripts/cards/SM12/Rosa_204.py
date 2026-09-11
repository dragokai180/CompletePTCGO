from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e2e69de4-d96f-5c7c-bb49-5585d70bc83d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name',
    display_name='Rosa',
    searchable_by=['Rosa', 'Supporter', 'Rosa'],
    subtypes=['Supporter'],
    collector_number=204,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for a Pokémon, a Trainer card, and a basic Energy card, reveal them, and put them into your hand. Then, shuffle your deck."),
    condition=standard_trainer_condition("You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn. Search your deck for a Pokémon, a Trainer card, and a basic Energy card, reveal them, and put them into your hand. Then, shuffle your deck."),
)
