from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b808a4cf-540f-528b-82ed-f44800402c15',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name',
    display_name='Magmortar',
    searchable_by=['Magmortar', 'Stage 1', 'Magmortar'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    family_id=126,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Twin Bursts',
            game_text='If Electivire is on your Bench, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
