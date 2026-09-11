from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96455027-716c-5f2d-835c-25f72fb63f6f',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    display_name='Staryu',
    searchable_by=['Staryu', 'Basic', 'Staryu'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=120,
    abilities=[
        Attack(
            title='Numbing Water',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
