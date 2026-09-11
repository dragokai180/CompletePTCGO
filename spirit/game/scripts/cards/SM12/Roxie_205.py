from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='82b11538-fc23-5c88-a138-4813890384d9',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Roxie.Name',
    display_name='Roxie',
    searchable_by=['Roxie', 'Supporter', 'Roxie'],
    subtypes=['Supporter'],
    collector_number=205,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard up to 2 Pokémon that aren't Pokémon-GX or Pokémon-EX from your hand. Draw 3 cards for each card you discarded in this way."),
    condition=standard_trainer_condition("Discard up to 2 Pokémon that aren't Pokémon-GX or Pokémon-EX from your hand. Draw 3 cards for each card you discarded in this way."),
)
