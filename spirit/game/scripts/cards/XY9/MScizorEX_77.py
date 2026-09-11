from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7185c0fa-936b-5722-8378-51c035146b06',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MScizorEX.Name',
    display_name='M Scizor-EX',
    searchable_by=['M Scizor-EX', 'MEGA', 'EX', 'MScizorEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=77,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name',
    family_id=212,
    abilities=[
        Attack(
            title='Iron Crusher',
            game_text="You may discard a Special Energy attached to your opponent's Active Pokémon or a Stadium card in play.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
