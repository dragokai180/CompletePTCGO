from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70ef0839-fc4e-5798-b068-4f8593cdde94',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SkarmoryEX.Name',
    display_name='Skarmory-EX',
    searchable_by=['Skarmory-EX', 'Basic', 'EX', 'SkarmoryEX'],
    subtypes=['Basic', 'EX'],
    collector_number=80,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title='Joust',
            game_text="Before doing damage, discard all Pokémon Tool cards attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Tailspin Piledriver',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
