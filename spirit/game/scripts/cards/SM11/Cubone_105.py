from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c69721bb-7c1e-5af1-97d7-25e21266ae3a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    display_name='Cubone',
    searchable_by=['Cubone', 'Basic', 'Cubone'],
    subtypes=['Basic'],
    collector_number=105,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=104,
    abilities=[
        Attack(
            title='Growl',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bonemerang',
            game_text='Flip 2 coins. This attack does 20 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
