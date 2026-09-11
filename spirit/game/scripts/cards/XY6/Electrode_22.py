from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='829b611a-a7a2-5bd2-973d-54763ea3c983',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name',
    display_name='Electrode',
    searchable_by=['Electrode', 'Stage 1', 'Electrode'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    family_id=100,
    abilities=[
        Attack(
            title='Continuous Tumble',
            game_text='Flip a coin until you get tails. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Energy Bomb',
            game_text='You may move all Energy from this Pokémon to your Benched Pokémon in any way you like.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
