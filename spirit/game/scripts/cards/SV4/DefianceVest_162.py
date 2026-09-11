from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='e63f2388-03a8-589b-9934-82b875982113',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DefianceVest.Name',
    display_name='Defiance Vest',
    searchable_by=['Defiance Vest', 'Pokémon Tool', 'DefianceVest'],
    subtypes=['Pokémon Tool'],
    collector_number=162,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("If you have more Prize cards remaining than your opponent, the Pokémon this card is attached to takes 40 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."),
)
