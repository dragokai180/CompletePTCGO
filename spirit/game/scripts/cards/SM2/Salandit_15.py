from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c443318-45f3-506e-8f97-f0dd6b756fb5',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    display_name='Salandit',
    searchable_by=['Salandit', 'Basic', 'Salandit'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=757,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Venoshock',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
