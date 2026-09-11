from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e30c41b3-6c58-5e1e-b340-934e28f2a518',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name',
    display_name='Luxray',
    searchable_by=['Luxray', 'Stage 2', 'Luxray'],
    subtypes=['Stage 2'],
    collector_number=34,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    family_id=403,
    abilities=[
        Attack(
            title='Fang Snipe',
            game_text='Your opponent reveals his or her hand. Discard a Trainer card you find there.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Wild Charge',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
