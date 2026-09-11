from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='693f32ca-9315-5f55-b29a-1b09be7116cb',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name',
    display_name='Donphan',
    searchable_by=['Donphan', 'Stage 1', 'Donphan'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    family_id=231,
    abilities=[
        Attack(
            title='Rock Hurl',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Double Spin',
            game_text='Flip 2 coins. This attack does 70 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
