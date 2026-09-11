from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='de23ef8b-9165-5340-87f7-3837ce1bc02f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name',
    display_name='Articuno',
    searchable_by=['Articuno', 'Basic', 'Articuno'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Attack(
            title='Chilling Sigh',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tri Edge',
            game_text='Flip 3 coins. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
)
