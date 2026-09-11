from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='d52715cc-ac2c-5677-be96-4193b0a7721a',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name',
    display_name='PlusPower',
    searchable_by=['PlusPower', 'Item', 'PlusPower'],
    subtypes=['Item'],
    collector_number=80,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach PlusPower to 1 of your Pokémon. Discard this card at the end of your turn. If the Pokémon PlusPower is attached to attacks, the attack does 10 more damage to the Defending Pokémon (before applying Weakness and Resistance).'),
    condition=standard_trainer_condition('Attach PlusPower to 1 of your Pokémon. Discard this card at the end of your turn. If the Pokémon PlusPower is attached to attacks, the attack does 10 more damage to the Defending Pokémon (before applying Weakness and Resistance).'),
)
