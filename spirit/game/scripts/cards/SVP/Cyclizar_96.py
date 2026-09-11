from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1d8a73b-eeee-5580-94c6-12580b60c38c',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name',
    display_name='Cyclizar',
    searchable_by=['Cyclizar', 'Basic', 'Cyclizar'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title='Flat-Out Dash',
            game_text='Flip a coin until you get tails. For each heads, draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Power Tackle',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
