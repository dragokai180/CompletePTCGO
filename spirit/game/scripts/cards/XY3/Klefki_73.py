from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66a8f7cd-d636-5c03-a4d3-5fa56f54a569',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name',
    display_name='Klefki',
    searchable_by=['Klefki', 'Basic', 'Klefki'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Ability(
            title='Secret Key',
            game_text="Each of your Fairy Pokémon's Resistance is now -40.",
            passive=standard_passive("Each of your Fairy Pokémon's Resistance is now -40."),
        ),
        Attack(
            title='Fairy Lock',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
