from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ec1b952-6236-5d6f-b03e-15f17c964b9d',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    display_name='Fuecoco',
    searchable_by=['Fuecoco', 'Basic', 'Fuecoco'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Super Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
