from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='45e4107e-e06b-5eac-8774-7e6add9fab5e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name',
    display_name='Wigglytuff',
    searchable_by=['Wigglytuff', 'Stage 1', 'Wigglytuff'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    family_id=39,
    abilities=[
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Expand',
            game_text="During your opponent's next turn, any damage done to Wigglytuff by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
