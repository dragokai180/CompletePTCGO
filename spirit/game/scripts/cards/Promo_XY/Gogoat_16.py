from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91735d3c-c6ea-5183-9e1f-dc7229cc45d8',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name',
    display_name='Gogoat',
    searchable_by=['Gogoat', 'Stage 1', 'Gogoat'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    family_id=672,
    abilities=[
        Attack(
            title='Push Down',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Forest Press',
            game_text='Flip a coin for each Grass Energy attached to this Pokémon. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
