from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92bb50ab-605d-5c2c-a3c4-5c63908f059f',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name',
    display_name='Exploud',
    searchable_by=['Exploud', 'Stage 2', 'Exploud'],
    subtypes=['Stage 2'],
    collector_number=82,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Cacophony',
            game_text="At the end of your opponent's next turn, discard the Defending Pokémon and all cards attached to it.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
