from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4fc49611-cfc4-5b65-a78b-5f3521041305',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name',
    display_name='Sudowoodo',
    searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=185,
    abilities=[
        Attack(
            title='Hit and Hide',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Elbow Strike',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
