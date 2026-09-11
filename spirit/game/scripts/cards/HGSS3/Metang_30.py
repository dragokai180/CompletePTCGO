from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e6372f7-7dbf-57cf-a565-a17b0bc940f5',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    display_name='Metang',
    searchable_by=['Metang', 'Stage 1', 'Metang'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name',
    family_id=374,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Double Smash',
            game_text='Flip 2 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
