from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab5edbcc-fea9-5f84-b5d3-dc99b0e4c3ea',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    display_name='Graveler',
    searchable_by=['Graveler', 'Stage 1', 'Graveler'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Rock Cannon',
            game_text='Flip a coin until you get tails. This attack does 40 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
