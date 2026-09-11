from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08d2d46a-a59d-55bc-94be-c2a3b694dd97',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name',
    display_name='Alomomola',
    searchable_by=['Alomomola', 'Basic', 'Alomomola'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=594,
    abilities=[
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Aqua Slash',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
