from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5ee0e1b4-cc2f-5626-9bb6-4548f3ba703d',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MistysWaterCommand.Name',
    display_name="Misty's Water Command",
    searchable_by=["Misty's Water Command", 'Supporter', 'MistysWaterCommand'],
    subtypes=['Supporter'],
    collector_number=63,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('Move any number of Water Energy from your Pokémon to your Psyduck, Horsea, Staryu, Starmie-GX, Magikarp, Gyarados, or Lapras in any way you like.'),
    condition=standard_trainer_condition('Move any number of Water Energy from your Pokémon to your Psyduck, Horsea, Staryu, Starmie-GX, Magikarp, Gyarados, or Lapras in any way you like.'),
)
