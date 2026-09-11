from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b993c3c8-b24f-52b5-a739-c1af7a20c51a',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name',
    display_name='Sudowoodo',
    searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=185,
    abilities=[
        Attack(
            title='Push Over',
            game_text='Does 20 damage times the amount of Fighting Energy attached to Sudowoodo.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Rumble',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
