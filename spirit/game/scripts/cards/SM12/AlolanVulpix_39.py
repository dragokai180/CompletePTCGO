from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='35e45315-4492-5ca1-8b87-ef0ffbb9d304',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    display_name='Alolan Vulpix',
    searchable_by=['Alolan Vulpix', 'Basic', 'AlolanVulpix'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Ability(
            title='Snowed In',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Gnaw',
            cost={},
            damage=10,
        ),
    ],
)
