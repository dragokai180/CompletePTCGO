from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aa90bff5-12e8-5921-a857-7f7c94f8e479',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name',
    display_name='Sharpedo-EX',
    searchable_by=['Sharpedo-EX', 'Basic', 'EX', 'SharpedoEX'],
    subtypes=['Basic', 'EX'],
    collector_number=91,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=319,
    abilities=[
        Attack(
            title='Hunt',
            game_text="Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Jagged Fang',
            game_text="Discard an Energy attached to this Pokémon. Then, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
