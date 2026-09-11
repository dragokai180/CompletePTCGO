from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db7352d0-b590-5aac-9f3e-d0e075063545',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MawileEX.Name',
    display_name='Mawile-EX',
    searchable_by=['Mawile-EX', 'Basic', 'EX', 'MawileEX'],
    subtypes=['Basic', 'EX'],
    collector_number=103,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title='Smack',
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
        ),
        Attack(
            title='Wonder Bomb',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
