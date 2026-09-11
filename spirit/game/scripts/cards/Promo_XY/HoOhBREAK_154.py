from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b8bd9e2-048d-5595-bcd0-4282e4145b7d',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOhBREAK.Name',
    display_name='Ho-Oh BREAK',
    searchable_by=['Ho-Oh BREAK', 'BREAK', 'HoOhBREAK'],
    subtypes=['BREAK'],
    collector_number=154,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name',
    family_id=250,
    abilities=[
        Attack(
            title='Shining Flame',
            game_text="This Pokémon can't use Shining Flame during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
