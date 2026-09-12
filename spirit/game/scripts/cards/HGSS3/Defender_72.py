from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='a286be9a-1393-5e9f-be55-82447c2d3133',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name',
    display_name='Defender',
    searchable_by=['Defender', 'Item', 'Defender'],
    subtypes=['Item'],
    collector_number=72,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Attach Defender to 1 of your Pokémon. Discard this card at the end of your opponent's next turn. Any damage done to the Pokémon Defender is attached to by attacks is reduced by 20 (after applying Weakness and Resistance)."),
    condition=standard_trainer_condition("Attach Defender to 1 of your Pokémon. Discard this card at the end of your opponent's next turn. Any damage done to the Pokémon Defender is attached to by attacks is reduced by 20 (after applying Weakness and Resistance)."),
)
