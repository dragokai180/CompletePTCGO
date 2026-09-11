from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2463937d-37d6-5657-aa43-c6195cfa6a5d',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name',
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", 'Supporter', 'GiovannisExile'],
    subtypes=['Supporter'],
    collector_number=174,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard up to 2 of your Benched Pokémon that have no damage counters on them and all cards attached to them.'),
    condition=standard_trainer_condition('Discard up to 2 of your Benched Pokémon that have no damage counters on them and all cards attached to them.'),
)
