from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e41b0182-0ab9-52f6-bd8e-43bf38609ded',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    display_name='Ponyta',
    searchable_by=['Ponyta', 'Basic', 'Ponyta'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=77,
    abilities=[
        Attack(
            title='Agility',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Flame Tail',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
