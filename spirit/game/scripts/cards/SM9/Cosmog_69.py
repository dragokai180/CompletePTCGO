from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bdd4b3c7-7dc5-5631-9afe-63c89914d814',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    display_name='Cosmog',
    searchable_by=['Cosmog', 'Basic', 'Cosmog'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=789,
    abilities=[
        Ability(
            title='Cosmic Guard',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Mumble',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
