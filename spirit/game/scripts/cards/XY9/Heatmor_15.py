from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df92643c-4e7c-5789-850a-5d3c8b2537c6',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name',
    display_name='Heatmor',
    searchable_by=['Heatmor', 'Basic', 'Heatmor'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=631,
    abilities=[
        Attack(
            title='Reinforced Flame',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 20 more damage.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
