from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd25d3fc-377b-5ca4-a3dc-4e8ddc33cacf',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name',
    display_name='Magmortar',
    searchable_by=['Magmortar', 'Stage 1', 'Magmortar'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    family_id=126,
    abilities=[
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=40,
        ),
        Attack(
            title='Volcanic Heat',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
