from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08af7e4c-02fd-5c5e-85b8-5a4c028d2dca',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    display_name='Oddish',
    searchable_by=['Oddish', 'Basic', 'Oddish'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=43,
    abilities=[
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Grass Knot',
            game_text="This attack does 20 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
