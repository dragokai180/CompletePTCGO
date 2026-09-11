from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f0e703b-e730-595d-97a6-e82c46e11947',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name',
    display_name='Bibarel',
    searchable_by=['Bibarel', 'Stage 1', 'Bibarel'],
    subtypes=['Stage 1'],
    collector_number=107,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    family_id=399,
    abilities=[
        Attack(
            title='Double Headbutt',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Hypno Headbutt',
            game_text='You may do 30 more damage. If you do, this Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
