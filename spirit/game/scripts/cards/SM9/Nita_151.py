from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='03b884f8-71a8-568c-af53-370d48ae2ebb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name',
    display_name='Nita',
    searchable_by=['Nita', 'Supporter', 'Nita'],
    subtypes=['Supporter'],
    collector_number=151,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if your opponent's Active Pokémon is a Basic Pokémon. Put an Energy from your opponent's Active Pokémon on top of their deck."),
    condition=standard_trainer_condition("You can play this card only if your opponent's Active Pokémon is a Basic Pokémon. Put an Energy from your opponent's Active Pokémon on top of their deck."),
)
