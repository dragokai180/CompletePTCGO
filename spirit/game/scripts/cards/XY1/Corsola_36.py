from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1ac05949-f4a7-5253-a4c0-54e798d35d0f',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name',
    display_name='Corsola',
    searchable_by=['Corsola', 'Basic', 'Corsola'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=222,
    abilities=[
        Attack(
            title='Refresh',
            game_text='Heal 30 damage and remove all Special Conditions from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spiny Rush',
            game_text='Flip a coin until you get tails. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
