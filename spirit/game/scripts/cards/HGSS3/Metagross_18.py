from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49e7b160-b515-52f9-8c55-647c740eff80',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name',
    display_name='Metagross',
    searchable_by=['Metagross', 'Stage 2', 'Metagross'],
    subtypes=['Stage 2'],
    collector_number=18,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Attack(
            title='Strength',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title='Quad Smash',
            game_text='Flip 4 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
