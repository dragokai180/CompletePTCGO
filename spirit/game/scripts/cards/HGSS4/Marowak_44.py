from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12edb6e5-d9d4-53c5-8ac7-728c83e9e18e',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name',
    display_name='Marowak',
    searchable_by=['Marowak', 'Stage 1', 'Marowak'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=104,
    abilities=[
        Attack(
            title='Bonemerang',
            game_text='Flip 2 coins. This attack does 60 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Bone Impact',
            game_text='If there is any Stadium card in play, this attack does 20 damage plus 60 more damage. Discard that Stadium card.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
