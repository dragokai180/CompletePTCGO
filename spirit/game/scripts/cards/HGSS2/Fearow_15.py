from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b91e858e-f1f6-5513-a55f-c9748a3483e5',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name',
    display_name='Fearow',
    searchable_by=['Fearow', 'Stage 1', 'Fearow'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    family_id=21,
    abilities=[
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Repeating Drill',
            game_text='Flip 5 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
