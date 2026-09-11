from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb4f1944-2253-5f8d-9b1d-0880d5d44761',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name',
    display_name='Jumpluff',
    searchable_by=['Jumpluff', 'Stage 2', 'Jumpluff'],
    subtypes=['Stage 2'],
    collector_number=6,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    family_id=187,
    abilities=[
        Attack(
            title='Mass Attack',
            game_text="Does 10 damage times the number of Pokémon in play (both yours and your opponent's).",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Guard',
            game_text="During your opponent's next turn, any damage done to Jumpluff by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
