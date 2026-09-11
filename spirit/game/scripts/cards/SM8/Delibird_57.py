from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a77ffac-7b03-54c1-8a45-1f9c8ace8230',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name',
    display_name='Delibird',
    searchable_by=['Delibird', 'Basic', 'Delibird'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=225,
    abilities=[
        Attack(
            title='Happy Delivery',
            game_text="Choose any number of your Benched Pokémon that don't already have a Pokémon Tool attached to them. For each of those Pokémon, search your deck for a Pokémon Tool card and attach it to that Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
