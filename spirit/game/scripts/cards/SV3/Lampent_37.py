from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ffce9e0-c7b8-58bd-973e-e6986a1be15a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    display_name='Lampent',
    searchable_by=['Lampent', 'Stage 1', 'Lampent'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name',
    family_id=607,
    abilities=[
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Alluring Fireball',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
