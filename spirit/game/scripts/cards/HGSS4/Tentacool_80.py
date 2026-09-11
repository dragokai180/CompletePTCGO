from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='73384e58-f4db-575a-9350-9b6f851232be',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    display_name='Tentacool',
    searchable_by=['Tentacool', 'Basic', 'Tentacool'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=72,
    abilities=[
        Attack(
            title='Gentle Wrap',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
