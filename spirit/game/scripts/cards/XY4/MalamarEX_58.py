from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1f8682c8-7904-5dda-a588-e2c88e2f9be5',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MalamarEX.Name',
    display_name='Malamar-EX',
    searchable_by=['Malamar-EX', 'Basic', 'EX', 'MalamarEX'],
    subtypes=['Basic', 'EX'],
    collector_number=58,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=687,
    abilities=[
        Ability(
            title='Hyper Hypnosis',
            game_text="When you attach an Energy from your hand to this Pokémon, you may use this Ability. Your opponent's Active Pokémon is now Asleep.",
            passive=standard_passive("When you attach an Energy from your hand to this Pokémon, you may use this Ability. Your opponent's Active Pokémon is now Asleep."),
        ),
        Attack(
            title='MAXamar',
            game_text='Flip a coin for each Energy attached to this Pokémon. This attack does 60 damage times the number of heads.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
