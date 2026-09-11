from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='34c81731-196f-51d0-b671-e79bf01a74b0',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokManiac.Name',
    display_name='Poké Maniac',
    searchable_by=['Poké Maniac', 'Supporter', 'PokManiac'],
    subtypes=['Supporter'],
    collector_number=204,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Pokémon that have a Retreat Cost of exactly 4, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Pokémon that have a Retreat Cost of exactly 4, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
