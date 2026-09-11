from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6afd4292-3547-5fbb-8875-a9c79967833c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name',
    display_name='Probopass',
    searchable_by=['Probopass', 'Stage 1', 'Probopass'],
    subtypes=['Stage 1'],
    collector_number=146,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    family_id=299,
    abilities=[
        Attack(
            title='Triple Nose',
            game_text='Flip 3 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Buster',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
