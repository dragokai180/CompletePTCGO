from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca03d688-c79c-598c-a055-fb314d629600',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name',
    display_name='Turtonator',
    searchable_by=['Turtonator', 'Basic', 'Turtonator'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=776,
    abilities=[
        Attack(
            title='Body Slam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
