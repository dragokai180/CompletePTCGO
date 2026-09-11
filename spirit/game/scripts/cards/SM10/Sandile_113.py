from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='babf7cc5-90d1-525f-a2a0-a800549319e9',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name',
    display_name='Sandile',
    searchable_by=['Sandile', 'Basic', 'Sandile'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=551,
    abilities=[
        Ability(
            title='Intimidating Fang',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 20 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 20 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
