from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d9a9a21-781e-5fb4-9ee8-06a1c2c0a703',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name',
    display_name='Goomy',
    searchable_by=['Goomy', 'Basic', 'Goomy'],
    subtypes=['Basic'],
    collector_number=91,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=704,
    abilities=[
        Ability(
            title='Sticky Membrane',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Pokémon's attacks cost Colorless more.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Pokémon's attacks cost Colorless more."),
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
