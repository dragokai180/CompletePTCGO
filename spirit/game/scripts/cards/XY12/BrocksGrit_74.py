from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='84280e62-8e67-5282-b954-38cc270be2f4',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name',
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", 'Supporter', 'BrocksGrit'],
    subtypes=['Supporter'],
    collector_number=74,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle 6 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.'),
    condition=standard_trainer_condition('Shuffle 6 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.'),
)
