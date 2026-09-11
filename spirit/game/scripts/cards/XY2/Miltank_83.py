from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93228f57-5824-5efa-9b01-f0cc92b805be',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name',
    display_name='Miltank',
    searchable_by=['Miltank', 'Basic', 'Miltank'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=241,
    abilities=[
        Attack(
            title='Powerful Friends',
            game_text='If you have any Stage 2 Pokémon on your Bench, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
