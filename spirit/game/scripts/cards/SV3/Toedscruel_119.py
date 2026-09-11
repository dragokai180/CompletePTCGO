from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6206dbd7-8956-5062-be74-a885661f4124',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name',
    display_name='Toedscruel',
    searchable_by=['Toedscruel', 'Stage 1', 'Toedscruel'],
    subtypes=['Stage 1'],
    collector_number=119,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    family_id=948,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title='Double Whip',
            game_text='Flip 2 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
