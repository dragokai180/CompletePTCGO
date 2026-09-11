from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5fcdd81a-af91-5b76-9a02-dc4e6c1c5ceb',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name',
    display_name='Hitmonchan',
    searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=107,
    abilities=[
        Attack(
            title='Detect',
            game_text="Flip a coin. If heads, prevent all effects of attack, including damage, done to Hitmonchan during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sky Uppercut',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
